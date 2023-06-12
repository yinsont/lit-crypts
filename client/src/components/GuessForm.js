import {React, useState} from 'react'
import ReactDOM from 'react-dom/client'

export default function GuessForm({puzzle, handleAttempts}){

    // console.log(guess)

    const [guess, setGuess] = useState("");
    const [select, setSelect] = useState('')
 
    const handleGuess = (value) => {
        // value.preventDefault()
      console.log(value)
      setGuess(value);
    };

    const handleSelect = (value) => {
        setSelect(value)
    }

    let new_puzzle = puzzle.join("");
    new_puzzle = new_puzzle.split("");

    const handleSubmit = (e) => {
        e.preventDefault()
        // console.log('hi')
        let attempt = {
            select: select,
            input: guess,
        }
        handleAttempts(attempt)
      }
    
    let keys = [...new Set(new_puzzle)]; //make new array have one of each character
    // console.log(keys)

    const optionCreator = keys.map((key) => {
        return <option value={key}>{key}</option>;
      });

    return(
        <form className="Game-Form" onSubmit = {handleSubmit} > 
            <select onChange = {e => handleSelect(e.target.value)}>
                <option></option>
                {optionCreator}
            </select>
            <input onChange = {e => handleGuess(e.target.value.toUpperCase())} value = {guess} placeholder='Take a Guess'></input>
            <button type = "submit" >Submit</button>
        </form>
    )
}

