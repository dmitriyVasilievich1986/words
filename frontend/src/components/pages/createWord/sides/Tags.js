import { Delimiter } from "../../components";
import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = classnames.bind(style);

function Tags(props) {
  const [allTags, setAllTags] = React.useState([]);

  React.useEffect(() => {
    axios
      .get("/api/tags/")
      .then((response) => {
        setAllTags(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <form style={{ position: "sticky", top: "10px" }}>
      <div className={cx("tags-row")}>
        {props.tags.length === 0 ? (
          <div>теги не привязаны</div>
        ) : (
          allTags
            .filter((at) => props.tags.includes(at.id))
            .map((tag) => (
              <span
                key={tag.id}
                className={cx("chosen")}
                onClick={() =>
                  props.setTags((prev) => prev.filter((p) => p !== tag.id))
                }
              >
                {tag.word}
              </span>
            ))
        )}
      </div>
      <Delimiter />
      <div className={cx("tags-row")}>
        {allTags
          .filter((at) => !props.tags.includes(at.id))
          .map((tag) => (
            <span
              key={tag.id}
              onClick={() => props.setTags((prev) => [...prev, tag.id])}
            >
              {tag.word}
            </span>
          ))}
      </div>
    </form>
  );
}

export default Tags;
