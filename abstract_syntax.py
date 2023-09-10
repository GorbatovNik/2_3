Grammar -> "$AXIOM" NTERM NLs ["$NTERM" {NTERM} NLs] "$TERM" TERM {Term} NLs Rule {Rule}.
Rule -> "$RULE" NTERM ASSIGN RightSideAlt {NLs RightSideAlt} {NL}.
RightSideAlt -> "$EPS" | ((NTERM | TERM) {NTERM | TERM}).
NLs -> NL {NL} | NL.
-----------------------------------------------------------------------------------
Grammar -> "$AXION" NTERM NLs NTermDeclOpt "$TERM" TERM TermList NLs Rule RuleList.
NTermDeclOpt -> "$NTERM" NTermList NLs.
NTermList -> NTERM NTermList | .
TermList -> TERM TermList | .
RuleList -> Rule RuleList | .
Rule -> "$RULE" NTERM ASSIGN RightSideAlt NLs RightSideAltListOpt NLsOpt.
RightSideAlt -> "$EPS" | ((NTERM | TERM) NTermOrTermListOpt).
NTermOrTermListOpt -> (NTERM | TERM) NTermOrTermListOpt | .
RightSideAltListOpt -> RightSideAlt NLs RightSideAltListOpt | .
NLs -> NL NLsOpt | NL.
NLsOpt -> NL NLsOpt | .
-----------------------------------------------------------------------------------
