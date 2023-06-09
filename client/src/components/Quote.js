import React, { useState, useEffect } from 'react';

function Quote() {
  const [quote, setQuote] = useState({});

  useEffect(() => {
    fetch('http://127.0.0.1:5555/quote')
    .then(response => response.json())
    .then(data => setQuote(data[0]));
  }, []);

  return (
    <>
      <p>{quote.author}</p>
      <p>{quote.text}</p>
    </>
  );
}

export default Quote;