export default function CryptedCard({ character, value, input = 't' }) {
  console.log(character, value)
  if (character == " ") {
    return <div className="Empty-Card"></div>;
  } else if ((character == value) || (input.toUpperCase() == value)){
    return (
      <div className="card-green" value={value}>
        <h1>{character.toUpperCase()}</h1>
      </div>
    );
  } else {
    return (
      <div className="card-red" value={value}>
        <h1>{character.toUpperCase()}</h1>
      </div>
    );
  }
}