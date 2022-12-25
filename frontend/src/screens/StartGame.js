import React, { useState } from 'react';
import styled from 'styled-components';
import { createGame } from '../api/globalService';
import { useNavigate } from 'react-router-dom';

const StartGame = () => {
  const [name, setName] = useState('');
  const navigate = useNavigate();
  const handleStartGame = async () => {
    try {
      const data = {
        player: name,
      };
      let res = await createGame(data);
      console.log(res);
      navigate('/main-board', { state: { ...res.data } });
    } catch (e) {
      console.log(e);
    }
  };

  return (
    <div>
      <Title> Robot vs. Dinosaur </Title>
      <Wrapper>
        <Input
          value={name}
          type="text"
          placeholder="Enter your name"
          onChange={(e) => setName(e.target.value)}
        />
        <Button onClick={handleStartGame}> Start Game </Button>
      </Wrapper>
    </div>
  );
};

const Title = styled.h1`
  color: Red;
  font-size: 50px;
  text-align: center;
`;

const Wrapper = styled.div`
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
  width: 50%;
  margin: 0 auto;
`;

const Input = styled.input`
  width: 100%;
  height: 40px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  box-sizing: border-box;
`;

const Button = styled.button`
  width: 100%;
  background-color: #4caf50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
`;

export default StartGame;
