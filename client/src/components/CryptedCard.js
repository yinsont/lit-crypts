export default function CryptedCard({ character, value, attempts }) {

  // console.log(attempts)

  for (let i = 0; i < attempts.length; i++) {
    if (attempts[i].select == character && attempts[i].input == value.original) {
      return (
        <div className="card-green" value={value}>
        <h1>{value.original.toUpperCase()}</h1>
      </div>
      )
    }
  }

  for (let i = 0; i < attempts.length; i++) {
    if (attempts[i].select == character && attempts[i].input != value.original) {
      return (
        <div className="card-red" value={character}>
        <h1>{value.encrypted.toUpperCase()}</h1>
      </div>
      )
    }
  }

  if (character == " ") {
    return <div className="Empty-Card"></div>;
  } else if ((character == value.original)) {
    return (
      <div className="card-green" value={value}>
        <h1>{value.original.toUpperCase()}</h1>
      </div>
    );
  } else {
    return (
      <div className="card" value={value}>
        <h1>{character.toUpperCase()}</h1>
      </div>
    );
  }
}
