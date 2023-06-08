import React from "react";
import Message from "./Message";

function MessageList({
  messages,
  currentUser,
  onMessageDelete,
  onUpdateMessage,
}) {
  return (
    <div className="list">
      <ul>
        {messages.map((message) => (
          <Message
            key={message.id}
            message={message}
            currentUser={currentUser}
            onMessageDelete={onMessageDelete}
            onUpdateMessage={onUpdateMessage}
          />
        ))}
      </ul>
    </div>
  );
}

export default MessageList;