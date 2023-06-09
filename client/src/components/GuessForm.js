import {React, useState} from 'react'
import ReactDOM from 'react-dom/client'

export default function GuessForm({keySelect, puzzle}){

    // console.log(guess)

    const [guess, setGuess] = useState("");

    const handleGuess = (value) => {
      setGuess(value);
    //   console.log(value)
    };

    let new_puzzle = puzzle.join("");
    new_puzzle = new_puzzle.split("");

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log('hi')
      }
    
    let keys = [...new Set(new_puzzle)]; //make new array have one of each character
    // console.log(keys)

    const optionCreator = keys.map((key) => {
        return <option value={key}>{key}</option>;
      });

    return(
        <form className="Game-Form" onSubmit = {handleSubmit} > 
            <select>
                <option></option>
                {optionCreator}
            </select>
            <input onChange = {e => handleGuess(e.target.value.toUpperCase())} value = {guess} placeholder='Take a Guess'></input>
            <button type = "submit" >Submit</button>
        </form>
    )
}

