import React, { useState, useEffect } from "react";
import styled from "styled-components";
import { FlatItem } from "./FlatItem";

const List = styled.ul`
  font-size: 22px;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const FlatsList = (props) => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      const response = await fetch("http://localhost:8000/api/flats-to-sell");
      console.log(response);
      const data = await response.json();
      setData(data);
      setLoading(false);
    };

    fetchData();
  }, []);

  return loading ? (
    <div>Loading...</div>
  ) : (
    <List>
      {data.map((item) => (
        <FlatItem url={item.image} text={item.title} key={item.id} />
      ))}
    </List>
  );
};
