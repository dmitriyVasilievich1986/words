import { useSearchParams } from "react-router-dom";
import classnames from "classnames/bind";
import style from "./style.scss";
import React from "react";

const cx = classnames.bind(style);

function WordsList({ infinitives }) {
  const [searchParams, setSearchParams] = useSearchParams();

  const selectedInfinitive = searchParams.get("infinitive");

  return (
    <div className={cx("list")}>
      <div className={cx("wrapper")}>
        {infinitives.map((infinitive) => (
          <div
            key={infinitive.id}
            onClick={() => setSearchParams({ infinitive: infinitive.id })}
            className={cx({ isSelected: selectedInfinitive == infinitive.id })}
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
