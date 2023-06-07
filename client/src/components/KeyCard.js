export default function KeyCard( {character} ){
    return(
        <div >

            <input className = "KeyCard" placeholder={character.toUpperCase()}></input>

            {/* <h1>{character}</h1> */}
        </div>
    )
}