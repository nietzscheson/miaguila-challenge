import pytest
from requests import put, get, post
import json

base_url = 'http://api:5000/v1/trips'
data_file = json.load(open('trip.json'));

def test_total_trips():

    total = get(base_url +  '/total').json()

    assert total['data'] == 593

def test_total_trips_per_city():
    
    uri = '/city/'

    bogota = get(base_url +  uri + 'Bogotá').json()
    medellin = get(base_url +  uri + 'Medellin').json()
    cali = get(base_url +  uri + 'Cali').json()
    cartagena = get(base_url +  uri + 'Cartagena').json()
    barranquilla = get(base_url +  uri + 'Barranquilla').json()
    
    assert bogota['data'] == 498
    assert medellin['data'] == 47
    assert cali['data'] == 29
    assert cartagena['data'] == 15
    assert barranquilla['data'] == 4

def test_trip_create():

    request = post(base_url, data = json.dumps(data_file));

    response = request.json()
    data = json.loads(response['data'])

    assert data['pickup_address'] == 'Cl. 90 #19-41, Bogotá, Colombia'
    assert data['country']['name'] == 'Colombia'
    assert data['city']['name'] == 'Bogotá'

def test_trip_update():

    ## Create Request

    request = post(base_url, data = json.dumps(data_file));

    response = request.json()
    data = json.loads(response['data'])

    ## Update Data

    data['pickup_address'] = 'Cl. 90 #19-41, Villavicencio, Colombia'

    ## Update Request

    request = put(base_url, data = json.dumps(data));

    response = request.json()
    data = json.loads(response['data'])

    assert data['pickup_address'] == 'Cl. 90 #19-41, Villavicencio, Colombia'