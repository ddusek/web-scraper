import React from "react";
import styled from "styled-components";

const Item = styled.li`
  list-style: none;
`;

const Image = styled.span`
  width: 400px;
  height: 300px;
  display: flex;
`;

export const FlatItem = (props) => {
  return (
    <Item>
      <p>{props.text}</p>
      <Image>
        <img src={props.url} alt="flat" />
      </Image>
    </Item>
  );
};
