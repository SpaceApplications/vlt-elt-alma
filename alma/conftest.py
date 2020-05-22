def pytest_addoption(parser):
    parser.addoption(
        '--driver',
        choices=('firefox', 'chrome', 'edge', 'safari'),
        required=True,
        help="Driver to use",
    )

    parser.addoption(
        '--ous_id',
        required=True,
        help="Observation Unit Set ID",
    )
