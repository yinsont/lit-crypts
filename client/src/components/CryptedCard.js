export default function CryptedCard({ character, value, input = 'ABCDE' }) {
  if (character === " ") {
    return <div className="Empty-Card"></div>;
  } else if (input.includes(character)) {
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