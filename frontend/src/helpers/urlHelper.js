import { BASE_URL } from '../constants';

export const formatURL = (url) => {
  console.log(BASE_URL);
  const apiUrl = BASE_URL + url;

  return apiUrl;
};
