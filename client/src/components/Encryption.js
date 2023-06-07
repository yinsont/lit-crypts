function Encryption(keyword = "JOHN", ciphertext = "TAR IS FOUND HERE") {
  const all_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

//   const keyword = "JOHN";
  let keyword1 = keyword.toUpperCase();
//   const ciphertext = "TAR IS FOUND HERE";

  // converts message to list
  const ct = ciphertext.toUpperCase().split("");

  // removes default elements
  const duplicates = (list) => {
    let key = [];
    for (let i = 0; i < list.length; i++) {
      if (!key.includes(list[i])) {
        key.push(list[i]);
      }
    }
    return key;
  };

  keyword1 = duplicates(keyword1);

  // Stores the encryption list
  const encrypting = duplicates(keyword1.concat(all_alphabets));

  // removes spaces from the encryption list
  for (let i = 0; i < encrypting.length; i++) {
    if (encrypting[i] === " ") {
      encrypting.splice(i, 1);
    }
  }

  // maps each element of the message to the encryption list and stores it in ciphertext
  let message = "";
  for (let i = 0; i < ct.length; i++) {
    if (ct[i] !== " ") {
      message = message + all_alphabets[encrypting.indexOf(ct[i])];
    } else {
      message = message + " ";
    }
  }
  
  
  return message
}

export default Encryption