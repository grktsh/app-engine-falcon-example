# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import falcon
import pytest

from app.entities.pets import Pet


def test_collection_get(client):
    pet_key1 = Pet(name='momo').put()
    pet_key2 = Pet(name='kuro').put()

    response = client.simulate_get('/api/v1/pets')

    assert response.status == falcon.HTTP_OK
    assert len(response.json) == 2
    assert response.json[0] == {'id': pet_key1.id(), 'name': 'momo'}
    assert response.json[1] == {'id': pet_key2.id(), 'name': 'kuro'}


def test_collection_post(client):
    response = client.simulate_post('/api/v1/pets', json={'name': 'hana'})

    pets = list(Pet.query())
    assert len(pets) == 1
    assert pets[0].name == 'hana'

    assert response.status == falcon.HTTP_CREATED
    assert response.json == {'id': pets[0].key.id(), 'name': 'hana'}


def test_collection_post_validation_error(client):
    response = client.simulate_post('/api/v1/pets', json={})

    assert response.status == falcon.HTTP_BAD_REQUEST


def test_item_get(client):
    pet_key = Pet(name='sora').put()

    response = client.simulate_get('/api/v1/pets/{}'.format(pet_key.id()))

    assert response.status == falcon.HTTP_OK
    assert response.json == {'id': pet_key.id(), 'name': 'sora'}


def test_item_get_not_found(client):
    response = client.simulate_get('/api/v1/pets/1')

    assert response.status == falcon.HTTP_NOT_FOUND


def test_item_patch(client):
    pet_key = Pet(name='tama').put()

    response = client.simulate_patch(
        '/api/v1/pets/{}'.format(pet_key.id()), json={'name': 'chibi'}
    )

    assert response.status == falcon.HTTP_OK
    assert response.json == {'id': pet_key.id(), 'name': 'chibi'}

    pets = list(Pet.query())
    assert len(pets) == 1
    assert pets[0].name == 'chibi'


def test_item_patch_without_name(client):
    pet_key = Pet(name='tama').put()

    response = client.simulate_patch(
        '/api/v1/pets/{}'.format(pet_key.id()), json={'foo': 'bar'}
    )

    assert response.status == falcon.HTTP_OK
    assert response.json == {'id': pet_key.id(), 'name': 'tama'}

    pets = list(Pet.query())
    assert len(pets) == 1
    assert pets[0].name == 'tama'


def test_item_patch_not_found(client):
    response = client.simulate_patch('/api/v1/pets/1', json={'name': 'cibi'})

    assert response.status == falcon.HTTP_NOT_FOUND


def test_item_delete(client):
    pet_key = Pet(name='mike').put()

    response = client.simulate_delete(
        '/api/v1/pets/{}'.format(pet_key.id()),
        headers={'X-API-Key': str('secret')},
    )

    assert response.status == falcon.HTTP_NO_CONTENT

    pets = list(Pet.query())
    assert len(pets) == 0


def test_item_delete_not_found(client):
    response = client.simulate_delete(
        '/api/v1/pets/1', headers={'X-API-Key': str('secret')}
    )

    assert response.status == falcon.HTTP_NOT_FOUND


@pytest.mark.parametrize('headers', [{'X-API-Key': str('unknown')}, {}])
def test_item_delete_when_invalid_api_key(client, headers):
    pet_key = Pet(name='mike').put()

    response = client.simulate_delete(
        '/api/v1/pets/{}'.format(pet_key.id()), headers=headers
    )

    assert response.status == falcon.HTTP_FORBIDDEN


@pytest.mark.parametrize('headers', [{'X-API-Key': str('unknown')}, {}])
def test_item_delete_not_found_when_invalid_api_key(client, headers):
    response = client.simulate_delete('/api/v1/pets/1', headers=headers)

    assert response.status == falcon.HTTP_FORBIDDEN
