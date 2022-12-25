import fetchAPI from '.';

export const createGame = (data) => {
  return fetchAPI({ url: 'games/initiate-game/start', method: 'POST', data });
};

export const getGame = (id) => {
  return fetchAPI({ url: `games/${id}`, method: 'GET' });
};

export const setRobot = (id, data) => {
  return fetchAPI({
    url: `games/initiate-game/${id}/set-robot`,
    method: 'POST',
    data,
  });
};

export const setDinosaur = (id, data) => {
  return fetchAPI({
    url: `games/initiate-game/${id}/set-dinosaur`,
    method: 'POST',
    data,
  });
};

export const moveAction = (id, data) => {
  return fetchAPI({
    url: `games/${id}/action/move`,
    method: 'POST',
    data,
  });
};

export const attackAction = (id) => {
  return fetchAPI({
    url: `games/${id}/action/attack`,
    method: 'POST',
  });
};
