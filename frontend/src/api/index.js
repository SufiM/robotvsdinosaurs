import axios from 'axios';
import { formatURL } from '../helpers/urlHelper';

const fetchAPI = function ({ url, method, data }) {
  return new Promise((resolve, reject) => {
    let defaultConfig = {
      method: method || 'GET',
      url: formatURL(url),
      headers: {
        'Content-Type': 'application/json',
      },
    };

    if (data) defaultConfig.data = data;

    axios(defaultConfig)
      .then((res) => {
        resolve(res);
      })
      .catch((error) => {
        reject({ error });
      });
  });
};

export default fetchAPI;
