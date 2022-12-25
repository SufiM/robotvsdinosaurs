import React from 'react';
import StartGame from '../screens/StartGame';
import MainBoard from '../screens/Game';

import { Route, Routes } from 'react-router-dom';

const MyRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<StartGame />} />
      <Route path="/main-board" element={<MainBoard />} />
    </Routes>
  );
};

export default MyRoutes;
