export default function CryptedCard({character, value, input = 'n'}){
    // console.log(value)
    if (character == ' '){
        return <div className="Empty-Card"></div>

    } else if (character == value || character == input.toUpperCase()){
        return(
            <div className="card-green" value = {value}>
                <h1>{character.toUpperCase()}</h1>
            </div>
        ) 
    } else {
        return(
            <div className="card-red" value = {value}>
                <h1>{character.toUpperCase()}</h1>
            </div>
    
        )
    }
}