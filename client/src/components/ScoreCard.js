import React, { useState } from "react";
import Timer from "./Timer/Timer"
import ControlButtons from "./ControlButtons/ControlButtons";

function ScoreCard({renderScore}){
const [isActive, setIsActive] = useState(false);
const [isPaused, setIsPaused] = useState(true);
const [time, setTime] = useState(0);

let finalTime; 
let finalScore;
let maxScore = 1000;
let maxTime = 300000

console.log("final time:", finalTime)
console.log("final score:", finalScore)
console.log("time:", time)

React.useEffect(() => {
        let interval = null;
 
        if (isActive && isPaused === false) {
            interval = setInterval(() => {
                setTime((time) => time + 10);
            }, 10);
        } else {
            clearInterval(interval);
        }
        return () => {
            clearInterval(interval);
        };
    }, [isActive, isPaused]);
 
    const handleStart = () => {
        setIsActive(true);
        setIsPaused(false);
    };
    const handlePauseResume = () => {
        setIsPaused(!isPaused);
    };
     const handleReset = () => {
        setIsActive(false);
        setTime(0);
    };

    if (isPaused && time > 0) {
        finalTime = time
        finalScore = Math.floor(maxScore - (time / maxTime) *maxScore) 
        renderScore(finalScore)
    }
    return (
        <>
            <Timer time= {time} />
            <ControlButtons
                active={isActive}
                isPaused={isPaused}
                handleStart={handleStart}
                handlePauseResume={handlePauseResume}
                handleReset={handleReset}
            />
        </>
    )
 }

 export default ScoreCard;