const environments = {
  DEVELOPMENT: {
    base_url: 'http://127.0.0.1:8000/api/v1/',
  },
};

export const REACT_APP_PUBLIC_ENVIRONMENT =
  process.env.REACT_APP_PUBLIC_ENVIRONMENT || 'DEVELOPMENT';
console.log('asdas', REACT_APP_PUBLIC_ENVIRONMENT);
export const environment = environments[REACT_APP_PUBLIC_ENVIRONMENT];

export const BASE_URL = environment.base_url;
