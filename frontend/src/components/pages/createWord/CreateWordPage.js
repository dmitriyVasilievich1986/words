import { useSearchParams } from "react-router-dom";
import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";
import axios from "axios";

import CreateWord from "./CreateWord";
import UpdateWord from "./UpdateWord";
import WordsList from "./WordsList";

import { Delimiter } from "../components";

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
    <div className={cx("container")}>
      <form>
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
    </div>
  );
}

function CreateWordPage() {
  const [infinitives, setInfinitives] = React.useState([]);
  const [tags, setTags] = React.useState([]);

  const [searchParams, setSearchParams] = useSearchParams();

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
      <div className={cx("side")}>
        <WordsList infinitives={infinitives} />
      </div>
      <div className={cx("center")}>
        {searchParams.get("infinitive") === null ? (
          <CreateWord
            setInfinitives={setInfinitives}
            tags={tags}
            setTags={setTags}
          />
        ) : (
          <UpdateWord
            pk={searchParams.get("infinitive")}
            setInfinitives={setInfinitives}
            setTags={setTags}
            tags={tags}
          />
        )}
      </div>
      <div className={cx("side")}>
        <Tags tags={tags} setTags={setTags} />
      </div>
    </div>
  );
}

export default CreateWordPage;
