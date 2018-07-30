# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import falcon

from app.entities.user import User


def test_collection_get(client):
    user_key1 = User(email='user1@example.com').put()
    user_key2 = User(email='user2@example.com').put()

    response = client.simulate_get('/api/v1/users')

    assert response.status == falcon.HTTP_OK
    assert len(response.json) == 2
    assert response.json[0] == {
        'id': user_key1.id(),
        'email': 'user1@example.com'
    }
    assert response.json[1] == {
        'id': user_key2.id(),
        'email': 'user2@example.com'
    }


def test_collection_post(client):
    response = client.simulate_post(
        '/api/v1/users', json={'email': 'user@example.com'}
    )

    users = list(User.query())
    assert len(users) == 1
    assert users[0].email == 'user@example.com'

    assert response.status == falcon.HTTP_CREATED
    assert response.json == {
        'id': users[0].key.id(),
        'email': 'user@example.com'
    }


def test_item_get(client):
    user_key = User(email='user@example.com').put()

    response = client.simulate_get('/api/v1/users/{}'.format(user_key.id()))

    assert response.status == falcon.HTTP_OK
    assert response.json == {'id': user_key.id(), 'email': 'user@example.com'}


def test_item_get_not_found(client):
    response = client.simulate_get('/api/v1/users/1')

    assert response.status == falcon.HTTP_NOT_FOUND
