export default function CryptedCard({ character, value, attempts }) {
  // console.log(value); // Output: "W
  console.log(value)
  console.log(attempts)
  

  if (character == " ") {
    return <div className="Empty-Card"></div>;
  } else if (character == value.original) {
    return (
      <div className="card-green" value={value}>
        <h1>{value.original.toUpperCase()}</h1>
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
