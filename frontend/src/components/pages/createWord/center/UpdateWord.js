import { useOutletContext, useParams } from "react-router-dom";
import classnames from "classnames/bind";
import { Card } from "../../components";
import style from "./style.scss";
import React from "react";
import axios from "axios";

const cx = classnames.bind(style);

function UpdateWord() {
  const props = { ...useParams(), ...useOutletContext() };

  const [personal_pronouns, setPersonal_pronouns] = React.useState([]);
  const [infinitive, setInfinitive] = React.useState(null);
  const [isLoading, setIsLoading] = React.useState(0);

  React.useEffect(() => {
    setIsLoading((prev) => prev + 1);
    Promise.all([
      axios.get(`/api/infinitive/${props.pk}/`),
      axios.get("/api/personal_pronoun/"),
    ])
      .then((response) => {
        const [infinitive, personal_pronouns] = response;
        setInfinitive({
          ...infinitive.data,
        });
        props.setTags(infinitive.data.tags.map((t) => t.tags));
        setPersonal_pronouns(personal_pronouns.data);
      })
      .catch((error) => {
        console.log(error);
      })
      .finally((_) => {
        setIsLoading((prev) => prev - 1);
      });
  }, [props.pk]);

  const submitHandler = () => {
    setIsLoading((prev) => prev + 1);
    axios
      .put(`/api/infinitive/${props.pk}/`, {
        ...infinitive,
        part_of_speech: infinitive.part_of_speech.id,
        tags: props.tags,
      })
      .then((response) => {
        setInfinitive((prev) => ({ ...prev, ...response.data }));
        props.setInfinitives((prev) =>
          prev.map((inf) => (inf.id === response.data.id ? response.data : inf))
        );
      })
      .catch((error) => {
        console.log(error);
      })
      .finally((_) => {
        setIsLoading((prev) => prev - 1);
      });
  };

  const updatePPVerb = ({ name, value }, ppId) => {
    setInfinitive((prev) => {
      const verb = prev.verb.map((v) =>
        v.personal_pronoun == ppId ? { ...v, [name]: value } : v
      );
      return { ...prev, verb };
    });
  };

  if (isLoading > 0 || infinitive === null) return <div>loading...</div>;
  return (
    <div className={cx("container")}>
      <form onSubmit={submitHandler}>
        <Card>
          <div className={cx("input-wrapper")}>
            <div className={cx("input-row")}>
              <label>Слово:</label>
              <input
                type="text"
                name="word"
                placeholder="Слово"
                value={infinitive.word}
                onChange={(e) =>
                  setInfinitive((prev) => ({ ...prev, word: e.target.value }))
                }
              />
            </div>
            <div className={cx("input-row")}>
              <label>Перевод:</label>
              <input
                type="text"
                name="translate"
                placeholder="Перевод"
                value={infinitive.translate}
                onChange={(e) =>
                  setInfinitive((prev) => ({
                    ...prev,
                    translate: e.target.value,
                  }))
                }
              />
            </div>
          </div>
        </Card>
        <Card>
          {personal_pronouns.map((personal_pronoun) => {
            const verb = infinitive.verb.find(
              (v) => v.personal_pronoun === personal_pronoun.id
            );
            return (
              <div
                key={personal_pronoun.id}
                className={cx("input-wrapper")}
                style={{ marginTop: "5px" }}
              >
                <div className={cx("input-row")}>
                  <label>{personal_pronoun.word}</label>
                  <input
                    type="text"
                    name="word"
                    placeholder="word"
                    value={verb.word}
                    onChange={(e) =>
                      updatePPVerb(e.target, personal_pronoun.id)
                    }
                  />
                </div>
                <div className={cx("input-row")}>
                  <label>{personal_pronoun.translate}</label>
                  <input
                    type="text"
                    name="translate"
                    placeholder="translate"
                    value={verb.translate}
                    onChange={(e) =>
                      updatePPVerb(e.target, personal_pronoun.id)
                    }
                  />
                </div>
              </div>
            );
          })}
        </Card>
        <div className={cx("send-button")}>
          <button>сохранить</button>
        </div>
      </form>
    </div>
  );
}

export default UpdateWord;
