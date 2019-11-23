import logging
import pytest

logger = logging.getLogger(__name__)

def test_get(nc):
    data = nc.accounts.get_all()
    logger.debug('data = %s', data)
    assert data, 'get all didnt work'

    internal_id = data[0]['internalId']
    data = nc.accounts.get(internalId=internal_id)
    logger.debug('data = %s', data)
    assert data, f'No object with internalId {internal_id}'

def test_post(nc):
    data = {}
    with pytest.raises(NotImplementedError) as ex:
        nc.accounts.post(data)
