import { credentialsTypes } from '../constants';
import credentialsService from '../../services/credentialsService';

const addCredential = data => dispatch => {
  return dispatch({
    type: credentialsTypes.ADD_CREDENTIAL,
    payload: credentialsService.addCredential(data)
  });
};

const getCredential = id => dispatch => {
  return dispatch({
    type: credentialsTypes.GET_CREDENTIAL,
    payload: credentialsService.getCredential(id)
  });
};

const getCredentials = (query = {}) => dispatch => {
  return dispatch({
    type: credentialsTypes.GET_CREDENTIALS,
    payload: credentialsService.getCredentials('', query)
  });
};

const updateCredential = (id, data) => dispatch => {
  return dispatch({
    type: credentialsTypes.UPDATE_CREDENTIAL,
    payload: credentialsService.updateCredential(id, data)
  });
};

const deleteCredential = id => dispatch => {
  return dispatch({
    type: credentialsTypes.DELETE_CREDENTIAL,
    payload: credentialsService.deleteCredential(id)
  });
};

const deleteCredentials = (ids = []) => dispatch => {
  return dispatch({
    type: credentialsTypes.DELETE_CREDENTIALS,
    payload: credentialsService.deleteCredential(ids)
  });
};

export {
  addCredential,
  deleteCredential,
  deleteCredentials,
  getCredential,
  getCredentials,
  updateCredential
};
