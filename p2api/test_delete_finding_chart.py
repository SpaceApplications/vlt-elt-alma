import p2api
import pytest
import requests

from common import API


api = API()
api.connect()


def test_cannot_delete_finding_chart_if_not_authenticated():
    response = requests.delete(f'{api.API_URL}/obsBlocks/0/findingCharts/0')
    assert response.status_code == 401


def test_cannot_delete_finding_chart_of_invalid_observing_block():
    ob_id = 'invalid'  # invalid observing block ID
    index = 1

    response = api.make_request(
        'DELETE', f'/obsBlocks/{ob_id}/findingCharts/{index}')

    assert response.status_code == 400


@pytest.mark.parametrize('invalid_index', [('invalid',), (0,), (6,)])
def test_cannot_delete_invalid_finding_chart(invalid_index):
    ob_id = api.create_observing_block();

    response = api.make_request(
        'DELETE', f'/obsBlocks/{ob_id}/findingCharts/{invalid_index}')

    assert response.status_code == 400


def test_cannot_delete_finding_chart_of_nonexisting_observing_block():
    ob_id = 0  # non-existing observing block ID
    index = 1

    response = api.make_request(
        'DELETE', f'/obsBlocks/{ob_id}/findingCharts/{index}')

    assert response.status_code == 404


def test_cannot_delete_nonexisting_finding_chart():
    ob_id = api.create_observing_block();
    index = 1  # non-existing finding chart index

    response = api.make_request(
        'DELETE', f'/obsBlocks/{ob_id}/findingCharts/{index}')

    assert response.status_code == 404


def test_delete_finding_chart():
    # connect to the API
    api = p2api.ApiConnection('demo', '52052', 'tutorial')

    # create observing block
    ob, _ = api.createOB(1448455, 'dummy observing block')
    ob_id = ob['obId']

    # add finding chart
    api.addFindingChart(ob_id, 'images/fc1.jpg')
    api.addFindingChart(ob_id, 'images/fc2.jpg')

    charts, _ = api.getFindingChartNames(ob_id)

    assert len(charts) == 2, 'Should have two finding charts'

    # delete 1st finding chart
    api.deleteFindingChart(ob_id, 1)

    charts, _ = api.getFindingChartNames(ob_id)

    assert len(charts) == 1, 'Should have two finding charts'
    assert charts[0] == 'fc2.jpg', 'Should keep the 2nd finding chart'
