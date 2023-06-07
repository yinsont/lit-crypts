// Javascript program for decoding the string
// which generate using classical cipher

// Original Set of letters
let plaintext = "1234567890,![]';<>$%#^@*&()ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// Function generates the encoded text
export function encoder(key) {
  let encoded = "";
  let arr = new Array(26).fill(0);

  // This loop inserts the keyword
  // at the start of the encoded string
  for (let i = 0; i < key.length; i++) {
    if (key[i] >= "A" && key[i] <= "Z") {
      // To check whether the character is inserted
      // earlier in the encoded string or not
      if (arr[key.charCodeAt(i) - 65] == 0) {
        encoded += key[i];
        arr[key.charCodeAt(i) - 65] = 1;
      }
    } else if (key[i] >= "a" && key[i] <= "z") {
      if (arr[key.charCodeAt(i) - 97] == 0) {
        encoded += String.fromCharCode(key.charCodeAt(i) - 32);
        arr[key.charCodeAt(i) - 97] = 1;
      }
    }
  }

  // This loop inserts the remaining
  // characters in the encoded string.
  for (let i = 0; i < 26; i++) {
    if (arr[i] == 0) {
      arr[i] = 1;
      encoded += String.fromCharCode(65 + i);
    }
  }
  return encoded;
}

// This function will decode the message
export function decipheredIt(msg, encoded) {
  // Hold the position of every character (A-Z)
  // from encoded string
  let enc = new Map();
  for (let i = 0; i < encoded.length; i++) {
    enc[encoded[i]] = i;
  }

  let decipher = "";

  // This loop deciphered the message.
  // Spaces, special characters and numbers remain same.
  for (let i = 0; i < msg.length; i++) {
    if (msg[i] >= "a" && msg[i] <= "z") {
      let pos = enc[msg.charCodeAt(i) - 32];
      decipher += plaintext[pos];
    } else if (msg[i] >= "A" && msg[i] <= "Z") {
      let pos = enc[msg[i]];
      decipher += plaintext[pos];
    } else {
      decipher += msg[i];
    }
  }
  return decipher;
}

// Driver code
// Hold the Keyword
let key = "walrus";
console.log("Keyword : ", key);

// Function call to generate encoded text
let encoded = encoder(key);

// Message that need to decode
let message = "I LOVE KUBERNETES";
console.log("Message before Deciphering : ", message);

// Function call to print deciphered text
console.log(decipheredIt(message, encoder(key))); //----encrypted sentence, comes out as str

// This code is contributed by poojaagarwal2.
