import React, { useState, useEffect } from "react";
import Game from "./Game.js";
import MessageList from "./Comment/MessageList.js";
import NewMessage from "./Comment/NewMessage.js";
import "./Comment/Message.css"
const testUser = { username: "Dfarlz97", id: 2 };
// let inputs = {};

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("http://localhost:5555/messages")
      .then((r) => r.json())
      .then((messages) => setMessages(messages));
  }, []);

  function handleAddMessage(newMessage) {
    setMessages([...messages, newMessage]);
  }

  function handleDeleteMessage(id) {
    const updatedMessages = messages.filter((message) => message.id !== id);
    setMessages(updatedMessages);
  }

  function handleUpdateMessage(updatedMessageObj) {
    const updatedMessages = messages.map((message) => {
      if (message.id === updatedMessageObj.id) {
        return updatedMessageObj;
      } else {
        return message;
      }
    });
    setMessages(updatedMessages);
  }

  const displayedMessages = messages.filter((message) =>
    message.body.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <main className="Title">
      <Game/>
      <MessageList
        messages={displayedMessages}
        currentUser={testUser}
        onMessageDelete={handleDeleteMessage}
        onUpdateMessage={handleUpdateMessage}
      />
      <NewMessage currentUser={testUser} onAddMessage={handleAddMessage} />
    </main>
  );
}
