import graphene

from .types import (
    PersonalPronounType,
    VerbInfinitiveType,
    NounInfinitiveType,
    DeclentionsType,
    PronounType,
    GenderType,
    VerbType,
    NounType,
)

from .models import (
    PersonalPronoun,
    VerbInfinitive,
    NounInfinitive,
    Declentions,
    Pronoun,
    Gender,
    Verb,
    Noun,
)


class PersonalPronounsQuery(graphene.ObjectType):
    prons = graphene.List(
        PersonalPronounType,
        plural=graphene.Boolean(),
        verb=graphene.BigInt(),
    )
    pron = graphene.Field(
        id=graphene.BigInt(required=True),
        type_=PersonalPronounType,
    )

    def resolve_prons(root, info, plural=None, verb=None):
        prons = PersonalPronoun.objects.all()
        prons = prons.filter(plural=plural) if plural else prons
        prons = prons.filter(verb=verb) if verb else prons
        return prons

    def resolve_pron(root, info, id):
        return PersonalPronoun.objects.get(id=id)


class GendersQuery(graphene.ObjectType):
    genders = graphene.List(
        GenderType,
        pronoun=graphene.BigInt(),
        noun=graphene.BigInt(),
    )
    gender = graphene.Field(
        id=graphene.BigInt(required=True),
        type_=GenderType,
    )

    def resolve_genders(root, info, pronoun=None, noun=None):
        gender = Gender.objects.all()
        gender = gender.filter(pronoun=pronoun) if pronoun else gender
        gender = gender.filter(noun=noun) if noun else gender
        return gender

    def resolve_gender(root, info, id):
        return Gender.objects.get(id=id)


class DeclentionsQuery(graphene.ObjectType):
    declentions = graphene.List(
        DeclentionsType,
        verb=graphene.BigInt(),
    )
    declention = graphene.Field(
        DeclentionsType,
        id=graphene.BigInt(required=True),
    )

    def resolve_declentions(root, info, verb=None):
        declentions = Declentions.objects.all()
        declentions = Declentions.filter(verb=verb) if verb else declentions
        return declentions

    def resolve_declention(root, info, id):
        return Declentions.objects.get(id=id)


class VerbInfinitiveQuery(graphene.ObjectType):
    verb_infinitives = graphene.List(
        VerbInfinitiveType,
        verb=graphene.BigInt(),
    )
    verb_infinitive = graphene.Field(
        VerbInfinitiveType,
        id=graphene.BigInt(required=True),
    )

    def resolve_verb_infinitives(root, info, verb=None):
        verb_infinitive = VerbInfinitive.objects.all()
        verb_infinitive = VerbInfinitive.filter(verb=verb) if verb else verb_infinitive
        return verb_infinitive

    def resolve_verb_infinitive(root, info, id):
        return VerbInfinitive.objects.get(id=id)


class VerbsQuery(graphene.ObjectType):
    verbs = graphene.List(
        VerbType,
        declention=graphene.BigInt(),
        pron=graphene.BigInt(),
    )
    verb = graphene.Field(
        VerbType,
        id=graphene.BigInt(required=True),
    )

    def resolve_verbs(root, info, declention=None, pron=None):
        verbs = Verb.objects.all()
        verbs = verbs.filter(declention=declention) if declention else verbs
        verbs = verbs.filter(pron=pron) if pron else verbs
        return verbs

    def resolve_verb(root, info, id):
        return Verb.objects.get(id=id)


class NounInfinitiveQuery(graphene.ObjectType):
    noun_infinitives = graphene.List(
        NounInfinitiveType,
        noun=graphene.BigInt(),
    )
    noun_infinitive = graphene.Field(
        NounInfinitiveType,
        id=graphene.BigInt(required=True),
    )

    def resolve_noun_infinitives(root, info, noun=None):
        noun_infinitive = NounInfinitive.objects.all()
        noun_infinitive = NounInfinitive.filter(noun=noun) if noun else noun_infinitive
        return noun_infinitive

    def resolve_noun_infinitive(root, info, id):
        return NounInfinitive.objects.get(id=id)


class NounQuery(graphene.ObjectType):
    nouns = graphene.List(
        NounType,
        declention=graphene.BigInt(),
        plural=graphene.Boolean(),
        gender=graphene.BigInt(),
    )
    noun = graphene.Field(
        NounType,
        id=graphene.BigInt(required=True),
    )

    def resolve_nouns(root, info, declention=None, plural=None, gender=None):
        noun = Noun.objects.all()
        noun = Noun.filter(declention=declention) if declention else noun
        noun = Noun.filter(plural=plural) if plural else noun
        noun = Noun.filter(gender=gender) if gender else noun
        return noun

    def resolve_noun(root, info, id):
        return Noun.objects.get(id=id)


class ProNounQuery(graphene.ObjectType):
    pronouns = graphene.List(
        PronounType,
        plural=graphene.Boolean(),
        gender=graphene.BigInt(),
    )
    pronoun = graphene.Field(
        PronounType,
        id=graphene.BigInt(required=True),
    )

    def resolve_pronouns(root, info, plural=None, gender=None):
        pronoun = Pronoun.objects.all()
        pronoun = Pronoun.filter(plural=plural) if plural else pronoun
        pronoun = Pronoun.filter(gender=gender) if gender else pronoun
        return pronoun

    def resolve_pronoun(root, info, id):
        return Pronoun.objects.get(id=id)


class Query(
    PersonalPronounsQuery,
    VerbInfinitiveQuery,
    NounInfinitiveQuery,
    DeclentionsQuery,
    ProNounQuery,
    GendersQuery,
    VerbsQuery,
    NounQuery,
):
    pass


schema = graphene.Schema(query=Query)
