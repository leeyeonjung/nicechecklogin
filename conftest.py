import pytest
from _pytest.runner import CallInfo
from _pytest.nodes import Item
from _pytest.terminal import TerminalReporter
import pytest_html

def pytest_html_results_table_header(cells):
    cells.insert(2, pytest_html.extras.html('<th>Dependency</th>'))
    cells.pop()

def pytest_html_results_table_row(report, cells):
    cells.insert(2, pytest_html.extras.html('<td>{}</td>'.format(getattr(report, 'dependency', ''))))
    cells.pop()

def pytest_runtest_makereport(item: Item, call: CallInfo):
    if 'dependency' in item.keywords:
        if call.when == 'call' and call.excinfo is None:
            item.keywords['dependency'].config.cache.set(item.nodeid, True)
        elif call.when == 'setup':
            dependencies = item.keywords['dependency'].kwargs.get('depends', [])
            for dep in dependencies:
                if not item.config.cache.get(dep, False):
                    pytest.skip(f"Dependency {dep} not met")
                    setattr(item, 'dependency', dep)
                    break

def pytest_terminal_summary(terminalreporter: TerminalReporter, exitstatus: int, config):
    total = len(terminalreporter.stats.get('passed', [])) + \
            len(terminalreporter.stats.get('failed', [])) + \
            len(terminalreporter.stats.get('skipped', [])) + \
            len(terminalreporter.stats.get('error', [])) + \
            len(terminalreporter.stats.get('xpassed', [])) + \
            len(terminalreporter.stats.get('xfailed', []))

    executed = len(terminalreporter.stats.get('passed', [])) + \
               len(terminalreporter.stats.get('failed', [])) + \
               len(terminalreporter.stats.get('xpassed', [])) + \
               len(terminalreporter.stats.get('xfailed', []))

    not_executed = total - executed

    if not_executed > 0:
        terminalreporter.write(f"\n{not_executed} tests were not executed and marked as errors.\n", red=True)
        for _ in range(not_executed):
            terminalreporter.stats.setdefault('error', []).append({
                'nodeid': 'ERROR: test not executed',
                'location': ('', 0, ''),
                'outcome': 'error',
                'longrepr': 'Test was not executed',
                'when': 'call'
            })