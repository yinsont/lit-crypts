import React from 'react'
import Game from "./Game.js"
import CommentBox from "./CommentBox.js"
import { Container, Header} from "semantic-ui-react";
export default function Home( {children} ) {

  return (
    

    <main className = "Title">
      <Game />
      <Container style={{ margin: 20 }}>

        <Header as="h1">Comment Section 💬</Header>

    {children}
      </Container>
      <CommentBox /> 
    </main>
  )
}