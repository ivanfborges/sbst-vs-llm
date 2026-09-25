"""Audit archived SBST × LLM evidence without invoking Java or rerunning PIT."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [ROOT / name / 'src/main/java/com/example/TriangleClassifier.java'
           for name in ('evosuite', 'llm')]
ARCHIVE = {
    'evosuite': 'evidencias/03-evosuite',
    'llm_refined': 'evidencias/04-llm',
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def metrics(side, folder):
    surefire = folder / ('03-surefire/TEST-com.example.TriangleClassifier_ESTest.xml'
                         if side == 'evosuite' else '04-surefire/TEST-com.example.TriangleClassifierTest.xml')
    jacoco = folder / ('04-jacoco/jacoco.xml' if side == 'evosuite' else '05-jacoco/jacoco.xml')
    pit = folder / ('05-pit/mutations.xml' if side == 'evosuite' else '06-pit/mutations.xml')
    log = folder / ('02-logs/02-mvn-pitest-mutationCoverage.txt'
                    if side == 'evosuite' else '03-logs/02-mvn-pitest-mutationCoverage.txt')
    suite = ET.parse(surefire).getroot()
    counters = {item.attrib['type']: {'covered': int(item.attrib['covered']),
                                       'missed': int(item.attrib['missed'])}
                for item in ET.parse(jacoco).getroot().findall('counter')}
    mutations = ET.parse(pit).getroot().findall('mutation')
    status = Counter(item.attrib['status'] for item in mutations)
    run_count = sum(int(item.attrib.get('numberOfTestsRun', '0')) for item in mutations)
    raw_log = log.read_bytes()
    archived_log = raw_log.decode('utf-16-le') if raw_log[:80].count(0) > 10 else raw_log.decode('utf-8', errors='replace')
    log_count = re.findall(r'Ran\s+(\d+)\s+tests\b', archived_log)
    if not log_count:
        raise ValueError(f'Missing PIT run count in {log}')
    if int(log_count[-1]) != run_count:
        raise ValueError(f'PIT log/XML run-count mismatch for {side}')
    if int(suite.attrib['failures']) or int(suite.attrib['errors']):
        raise ValueError(f'Archived Surefire suite failed: {side}')
    if sum(status.values()) != 25 or status['KILLED'] + status['SURVIVED'] + status['NO_COVERAGE'] != 25:
        raise ValueError(f'Unexpected archived mutation statuses for {side}: {status}')
    return {
        'surefire': {'tests': int(suite.attrib['tests']), 'failures': int(suite.attrib['failures']),
                     'errors': int(suite.attrib['errors']), 'seconds': float(suite.attrib['time'])},
        'jacoco': {key: counters[key] for key in ('INSTRUCTION', 'BRANCH', 'LINE', 'METHOD')},
        'pit': {'mutations': len(mutations), 'status': dict(sorted(status.items())),
                'test_executions_sum': run_count},
        'evidence_sha256': {'surefire': sha(surefire), 'jacoco': sha(jacoco), 'pit': sha(pit)},
    }


def main():
    hashes = [sha(path) for path in SOURCES]
    historical = ROOT / 'evidencias/02-classe-alvo/TriangleClassifier.java'
    if len(set(hashes + [sha(historical)])) != 1:
        raise ValueError('Target source differs between arms or historical evidence')
    report = {'target_source_sha256': hashes[0],
              'arms': {side: metrics(side, ROOT / folder) for side, folder in ARCHIVE.items()}}
    old_pit = ROOT / 'reports/llm/pit/mutations.xml'
    old_mutations = ET.parse(old_pit).getroot().findall('mutation')
    old_status = Counter(item.attrib['status'] for item in old_mutations)
    report['other_llm_pit_copy'] = {
        'path': old_pit.relative_to(ROOT).as_posix(),
        'sha256': sha(old_pit),
        'status': dict(sorted(old_status.items())),
        'test_executions_sum': sum(int(item.attrib.get('numberOfTestsRun', '0')) for item in old_mutations),
    }
    if old_status != Counter(report['arms']['llm_refined']['pit']['status']):
        raise ValueError('Other LLM PIT copy has different mutation statuses')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
