import pytest
from requests import put, get, post
import json

base_url = 'http://api:5000/v1/trips'
data_file = json.load(open('trip.json'));

def test_total_trips():

    total = get(base_url +  '/total').json()

    assert total['data'] == 593

def test_total_trips_per_city():
    
    uri = '/cities/'

    bogota = get(base_url +  uri + 'Bogotá').json()
    medellin = get(base_url +  uri + 'Medellin').json()
    cali = get(base_url +  uri + 'Cali').json()
    cartagena = get(base_url +  uri + 'Cartagena').json()
    barranquilla = get(base_url +  uri + 'Barranquilla').json()
    pasto = get(base_url +  uri + 'Pasto')
    
    assert bogota['data'] == 498
    assert medellin['data'] == 47
    assert cali['data'] == 29
    assert cartagena['data'] == 15
    assert barranquilla['data'] == 4
    assert pasto.status_code == 204

def test_trip_create():

    request = post(base_url, data = json.dumps(data_file));

    response = request.json()
    data = json.loads(response['data'])

    assert data['start']['pickup_address'] == 'Cl. 90 #19-41, Bogotá, Colombia'
    assert data['country']['name'] == 'Colombia'
    assert data['city']['name'] == 'Bogotá'

def test_trip_update():

    ## Create Request

    request = post(base_url, data = json.dumps(data_file));

    response = request.json()
    data = json.loads(response['data'])

    ## Update Data

    data['start']['pickup_address'] = 'Cl. 90 #19-41, Villavicencio, Colombia'

    ## Update Request

    id = data['_id']['$oid']

    del data['_id'] 

    request = put(base_url + '/' + id, data = json.dumps(data));

    response = request.json()

    data = json.loads(response['data'])

    assert data['start']['pickup_address'] == 'Cl. 90 #19-41, Villavicencio, Colombia'