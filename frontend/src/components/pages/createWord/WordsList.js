import { useSearchParams } from "react-router-dom";
import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";

const cx = classnames.bind(style);

function WordsList({ infinitives }) {
  const [searchParams, setSearchParams] = useSearchParams();
  const [search, setSearch] = React.useState("");

  const selectedInfinitive = searchParams.get("infinitive");

  return (
    <div className={cx("list")}>
      <div className={cx("search")}>
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>
      <div className={cx("wrapper")}>
        {infinitives
          .filter(
            (i) =>
              search === "" ||
              i.word.toLowerCase().includes(search.toLowerCase()) ||
              i.translate.toLowerCase().includes(search.toLowerCase())
          )
          .map((infinitive) => (
            <div
              key={infinitive.id}
              onClick={() => setSearchParams({ infinitive: infinitive.id })}
              className={cx({
                isSelected: selectedInfinitive == infinitive.id,
              })}
            >
              <div>
                {infinitive.word} / {infinitive.translate}
              </div>
            </div>
          ))}
      </div>
    </div>
  );
}

export default WordsList;
