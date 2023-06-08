import React, { useState } from "react";

function NewMessage({ currentUser, onAddMessage }) {
  const [body, setBody] = useState("");

  function handleSubmit(e) {
    e.preventDefault();

    fetch("http://localhost:5000/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: currentUser.username,
        body: body,
      }),
    })
      .then((r) => r.json())
      .then((newMessage) => {
        onAddMessage(newMessage);
        setBody("");
      });
  }

  return (
    <form className="new-message" onSubmit={handleSubmit}>
      <input
        type="text"
        name="body"
        autoComplete="off"
        placeholder="Comment!"
        value={body}
        onChange={(e) => setBody(e.target.value)}
      />
      <button type="submit">Send</button>
    </form>
  );
}

export default NewMessage;