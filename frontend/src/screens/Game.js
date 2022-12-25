import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { useLocation } from 'react-router-dom';
import {
  getGame,
  setRobot,
  setDinosaur,
  moveAction,
  attackAction,
} from '../api/globalService';
import { useNavigate } from 'react-router-dom';

const MOVE_ACTION = 'move';
const ATTACK_ACTION = 'attack';

const MainBoard = () => {
  const [boardGameData, setBoardGameData] = useState({});
  const [step, setStep] = useState(0);
  const [dinosaurPositions, setDinosaurPositions] = useState([]);
  const [robotPosition, setRobotPosition] = useState(null);
  const location = useLocation();
  const navigate = useNavigate();

  const getBoard = async () => {
    try {
      let res = await getGame(location.state.id);
      setBoardGameData(res.data);
      setRobotPosition(getRobotPosition(res.data.board));
      setDinosaurPositions(getDinosaurPositions(res.data.board));
      setStep(res.data.status);
    } catch (e) {
      console.log(e);
    }
  };

  const getRobotPosition = (board) => {
    let robotPosition = null;
    board.cells.forEach((row, i) => {
      row.forEach((cell, j) => {
        if (cell === 1) {
          robotPosition = [i, j];
        }
      });
    });

    return robotPosition;
  };

  const getDinosaurPositions = (board) => {
    let dinosaurPositions = [];
    board.cells.forEach((row, i) => {
      row.forEach((cell, j) => {
        if (cell === 2) {
          dinosaurPositions.push([i, j]);
        }
      });
    });

    return dinosaurPositions;
  };

  const handelMoveRobot = async (direction) => {
    try {
      let res = await moveAction(location.state.id, {
        action: {
          action_type: MOVE_ACTION,
          direction: direction,
        },
      });

      setBoardGameData(res.data);
      setRobotPosition(getRobotPosition(res.data.board));
    } catch (e) {
      console.log(e);
    }
  };

  const handelAttack = async () => {
    try {
      let res = await attackAction(location.state.id, {
        action: {
          action_type: ATTACK_ACTION,
        },
      });

      setBoardGameData((boardGameData) => ({
        ...boardGameData,
        board: {
          ...boardGameData.board,
          cells: boardGameData.board.cells.map((row, i) =>
            row.map((cell, j) => {
              if (i - robotPosition[0] === 1 && j - robotPosition[1] === 0) {
                return 3;
              }
              if (i - robotPosition[0] === -1 && j - robotPosition[1] === 0) {
                return 3;
              }
              if (i - robotPosition[0] === 0 && j - robotPosition[1] === 1) {
                return 3;
              }
              if (i - robotPosition[0] === 0 && j - robotPosition[1] === -1) {
                return 3;
              }

              return cell;
            })
          ),
        },
      }));

      setTimeout(() => {
        setBoardGameData(res.data);
        setDinosaurPositions(getDinosaurPositions(res.data.board));
      }, 1000);
    } catch (e) {
      console.log(e);
    }
  };

  const handleCellClick = async (i, j) => {
    if (step === 0) {
      await setRobot(location.state.id, {
        robot_position: [i, j],
      });

      setRobotPosition([i, j]);
      setStep(1);
    } else if (step === 1) {
      if (robotPosition[0] === i && robotPosition[1] === j) {
        alert('Robot and Dinosaur can not be in same position');
        return;
      }

      setDinosaurPositions((dinosaurPositions) => [
        ...dinosaurPositions,
        [i, j],
      ]);
    }
  };

  const handleSubmitDinosaurs = async () => {
    try {
      await setDinosaur(location.state.id, {
        dinosaurs_positions: dinosaurPositions,
      });
      setStep(2);
    } catch (e) {
      console.log(e);
    }
  };

  const handleRenderCellContent = (i, j, cell) => {
    if (cell == 3) {
      return '💥';
    } else if (
      cell == 1 ||
      (robotPosition && robotPosition[0] === i && robotPosition[1] === j)
    ) {
      return '🤖';
    } else if (
      cell == 2 ||
      (dinosaurPositions.length > 0 &&
        dinosaurPositions.find(
          (position) => position[0] === i && position[1] === j
        ))
    ) {
      return '🦖';
    } else {
      return '';
    }
  };

  const handleRestartGame = async () => {
    try {
      navigate('/');
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getBoard();
  }, []);

  if (boardGameData?.status === 3) {
    return (
      <Restart>
        <Title>
          <span>Game Over</span>
        </Title>
        <button onClick={() => handleRestartGame()}>Restart</button>
      </Restart>
    );
  }

  return (
    <div>
      <Title> Robot VS Dinosaur </Title>
      <Wrapper>
        <Board>
          {boardGameData?.board?.cells?.map((row, i) => {
            return (
              <div key={i} className="row">
                {row.map((cell, j) => {
                  return (
                    <Cell key={j} onClick={() => handleCellClick(i, j)}>
                      {handleRenderCellContent(i, j, cell)}
                    </Cell>
                  );
                })}
              </div>
            );
          })}
        </Board>
        <Console>
          <h2>Game Console</h2>
          {step === 0 && (
            <div>
              <h3>Choose Robot's position</h3>
            </div>
          )}

          {step === 1 && (
            <div>
              <h3>Choose Dinosaur's position</h3>

              <button onClick={handleSubmitDinosaurs}>
                Done <span>👍</span>
              </button>
            </div>
          )}
          {step === 2 && (
            <MoveButton>
              <button onClick={() => handelMoveRobot('N')}>Up</button>
              <div className="three-bottom">
                <button onClick={() => handelMoveRobot('W')}>Left</button>
                <button onClick={() => handelMoveRobot('S')}>Down</button>
                <button onClick={() => handelMoveRobot('E')}>Right</button>
              </div>
              <button className="attack-button" onClick={() => handelAttack()}>
                Attack
              </button>
            </MoveButton>
          )}
        </Console>
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
  background-color: #f2f2f2;
  padding: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const Board = styled.div`
  position: relative;
  display: flex;
`;

const Cell = styled.div`
  border: 1px solid black;
  width: 50px;
  height: 50px;
  font-size: 35px;
`;

const Console = styled.div`
  margin-left: 50px;
  border: 1px solid black;
  text-align: center;

  h2 {
    color: green;
`;

const MoveButton = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  button {
    width: 50px;
    height: 50px;
    margin: 1px;
  }

  .three-bottom {
    display: flex;
  }

  .attack-button {
    margin-top: 10px;
    width: 100%;
    height: 50px;
    background-color: red;
    color: white;
  }
`;

const Restart = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  h1 {
    color: red;
  }
  button {
    width: 100px;
    height: 50px;
    background-color: green;
    color: white;
  }
`;

export default MainBoard;
