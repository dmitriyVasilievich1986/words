import className from "classnames";
import style from "./style.scss";
import React from "react";

const cx = className.bind(style);

function Select({ multiple, value, onChange, options, name }) {
  const [highlightedIndex, setHighlightedIndex] = React.useState(0);
  const [isOpen, setIsOpen] = React.useState(false);

  React.useEffect(() => {
    if (!isOpen) setHighlightedIndex(0);
  }, [isOpen]);

  function clearOptions() {
    multiple ? onChange([]) : onChange(null);
  }

  function isOptionSelected(option) {
    return multiple ? value.includes(option.id) : option.id === value;
  }

  function selectOption(option) {
    if (multiple) {
      onChange(
        value.includes(option.id)
          ? value.filter((v) => v !== option.id)
          : [...value, option.id]
      );
    } else {
      if (option.id !== value) onChange(option.id);
    }
  }

  if (options === null || options?.length === 0) return null;
  return (
    <div
      onClick={() => setIsOpen((prev) => !prev)}
      className={cx("select-container")}
      onBlur={() => setIsOpen(false)}
      tabIndex={0}
    >
      {name && <span className={cx("select-name")}>{name}</span>}

      <span className={cx("value")}>
        {multiple
          ? options
              .filter((o) => value.includes(o.id))
              .map((v) => (
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    selectOption(v);
                  }}
                  className={cx("option-badge")}
                  key={v.id}
                >
                  {v.word}
                  <span>&times;</span>
                </button>
              ))
          : options.find((o) => o.id === value)?.word}
      </span>

      <button
        className={cx("clear-btn")}
        onClick={(e) => {
          e.stopPropagation();
          e.preventDefault();
          clearOptions();
        }}
      >
        &times;
      </button>

      <div className={cx("divider")}></div>
      <div className={cx("caret")}></div>

      <ul className={cx("options", { isOpen })}>
        {options.map((option, index) => (
          <li
            onClick={(e) => {
              e.stopPropagation();
              selectOption(option);
              setIsOpen(false);
            }}
            className={cx("option", {
              selected: isOptionSelected(option),
              highlighted: index === highlightedIndex,
            })}
            onMouseEnter={() => setHighlightedIndex(index)}
            key={option.id}
          >
            {option.word}
            {option.count && (
              <span className={cx("count")}>{option.count}</span>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Select;
