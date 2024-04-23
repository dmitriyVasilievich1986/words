import { SideContainer } from "../components";
import { Outlet } from "react-router-dom";
import { WordsList, Tags } from "./sides";
import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = classnames.bind(style);

function CreateWordPage() {
  const [infinitives, setInfinitives] = React.useState([]);
  const [tags, setTags] = React.useState([]);

  React.useEffect(() => {
    axios
      .get("/api/infinitive/")
      .then((response) => {
        setInfinitives(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className={cx("page")}>
      <SideContainer>
        <WordsList infinitives={infinitives} />
      </SideContainer>
      <div className={cx("center")}>
        <Outlet
          context={{
            setInfinitives: setInfinitives,
            setTags: setTags,
            tags: tags,
          }}
        />
      </div>
      <SideContainer className="margin">
        <Tags tags={tags} setTags={setTags} />
      </SideContainer>
    </div>
  );
}

export default CreateWordPage;
