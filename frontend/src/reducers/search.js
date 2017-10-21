import { SEARCH_REQUEST, SEARCH_RESPONSE, SHOW_SEARCH_BOX, HIDE_SEARCH_BOX } from '../actions/search';

export function search(state = {
  showSearchResults: false,
  machineGeneratedResult: null,
  similarQuestions: []
}, action) {
  switch (action.type) {
    case SEARCH_REQUEST:
      return state;
    case SEARCH_RESPONSE:
      return {
        ...state,
        showSearchResults: true,
        machineGeneratedResult: action.machineGeneratedResult,
        similarQuestions: action.similarQuestions,
      };
    default:
      return state;
  }
};

export function showSearchBox(state = {
  showSearchBox: false
}, action) {
  switch (action.type) {
    case SHOW_SEARCH_BOX:
      return { ...state, showSearchBox: true };
    default:
      return state;
  }
}

export function hideSearchBox(state = {
  showSearchBox: true
}, action) {
  switch (action.type) {
    case HIDE_SEARCH_BOX:
      return { ...state, showSearchBox: false };
    default:
      return state;
  }
}