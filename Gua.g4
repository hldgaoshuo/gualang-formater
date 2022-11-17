grammar Gua;

block
    : statement* returnStatement?
    ;

statement
    : VAR IDENTIFIER '=' expression # LabelStatementDefinition
    | CON IDENTIFIER '=' expression # LabelStatementConst
    | VAR THIS '.' IDENTIFIER '=' expression # LabelStatementThisDefinition
    | CON THIS '.' IDENTIFIER '=' expression # LabelStatementThisConst
    | VAR CLASS '.' IDENTIFIER '=' expression # LabelStatementClassDefinition
    | CON CLASS '.' IDENTIFIER '=' expression # LabelStatementClassConst
    | WHILE '(' expression ')' '{' block '}' # LabelStatementWhile
    | BREAK # LabelStatementBreak
    | CONTINUE # LabelStatementContinue
    | IF '(' expression ')' '{' block '}' # LabelStatementIf
    | IF '(' expression ')' '{' block '}' ELSE '{' block '}' # LabelStatementIfElse
    | IF '(' expression ')' '{' block '}' elseIfClause+ # LabelStatementIfElseIf
    | IF '(' expression ')' '{' block '}' elseIfClause+ ELSE '{' block '}' # LabelStatementIfElseIfElse
    | FOR '(' forInitClause ';' expression ';' forAssignClause ')' '{' block '}' # LabelStatementFor
    | IDENTIFIER op=('+=' | '-=' | '*=' | '/=' | '=') expression # LabelStatementAssignVar
    | THIS '.' IDENTIFIER op=('+=' | '-=' | '*=' | '/=' | '=') expression # LabelStatementAssignThisField
    | CLASS '.' IDENTIFIER op=('+=' | '-=' | '*=' | '/=' | '=') expression # LabelStatementAssignClassField
    | IDENTIFIER '.' IDENTIFIER op=('+=' | '-=' | '*=' | '/=' | '=') expression # LabelStatementAssignField
    | CON IDENTIFIER '=' FUNCTION '(' formalParameters ')' '{' block '}' # LabelStatementFunction
    | CON IDENTIFIER '=' CLASS '(' formalParameters ')' '{' block '}' # LabelStatementClass
    | CON CLASS '.' IDENTIFIER '=' FUNCTION '(' formalParameters ')' '{' block '}' # LabelStatementClassFunction
    | functionCallItem # LabelStatementFunctionCall
    | functionCallItem ('.' clainItem)+ # LabelStatementFunctionCallChain
    | methodCallItem # LabelStatementMethodCall
    | methodCallItem ('.' clainItem)+ # LabelStatementMethodCallChain
    ;

returnStatement
    : RETURN expression
    ;

elseIfClause
    : ELSE IF '(' expression ')' '{' block '}'
    ;

forInitClause
    : VAR IDENTIFIER '=' expression
    ;

forAssignClause
    : IDENTIFIER op=('+=' | '-=' | '*=' | '/=' | '=') expression
    ;

expression
    : expression op=('*' | '/' | '%') expression # LabelExpressionMulDivMod
    | expression op=('+' | '-') expression # LabelExpressionAddSub
    | expression op=('<<' | '>>') expression # LabelExpressionBitMove
    | expression '&' expression # LabelExpressionBitAnd
    | '~' expression # LabelExpressionBitNot
    | expression '|' expression # LabelExpressionBitOr
    | expression op=('<' | '>' | '<=' | '>=' | '==' | '!=') expression # LabelExpressionRelation
    | expression 'and' expression # LabelExpressionAnd
    | expression 'or' expression # LabelExpressionOr
    | THIS '.' IDENTIFIER # LabelExpressionThisFieldCall
    | THIS ('.' clainItem)+ # LabelExpressionThisFieldCallChain
    | CLASS '.' IDENTIFIER # LabelExpressionClassFieldCall
    | CLASS ('.' clainItem)+ # LabelExpressionClassFieldCallChain
    | IDENTIFIER '.' IDENTIFIER # LabelExpressionFieldCall
    | IDENTIFIER ('.' clainItem)+ # LabelExpressionFieldCallChain
    | functionCallItem # LabelExpressionFunctionCall
    | functionCallItem ('.' clainItem)+ # LabelExpressionFunctionCallChain
    | methodCallItem # LabelExpressionMethodCall
    | methodCallItem ('.' clainItem)+ # LabelExpressionMethodCallChain
    | '[' (expression)? (',' expression)* ']' # LabelExpressionArray
    | '{' (mapItem)? (',' mapItem)* '}' #LabelExpressionMap
    | NULL # LabelExpressionLiteralNull
    | FLOAT # LabelExpressionLiteralFloat
    | INT # LabelExpressionLiteralInt
    | BOOL # LabelExpressionLiteralBool
    | STRING # LabelExpressionLiteralString
    | IDENTIFIER # LabelExpressionIdentifier
    ;

mapItem
    : STRING ':' expression
    ;

functionCallItem
    : IDENTIFIER '(' actualParameters ')'
    ;

methodCallItem
    : IDENTIFIER '.' IDENTIFIER '(' actualParameters ')'
    ;

clainItem
    : IDENTIFIER
    | functionCallItem
    ;

formalParameters
    : (IDENTIFIER)? (',' IDENTIFIER)*
    ;

actualParameters
    : (expression)? (',' expression)*
    ;

VAR
    : 'var'
    ;

CON
    : 'con'
    ;

THIS
    : 'this'
    ;

CLASS
    : 'class'
    ;

IF
    : 'if'
    ;

ELSE
    : 'else'
    ;

WHILE
    : 'while'
    ;

FOR
    : 'for'
    ;

BREAK
    : 'break'
    ;

CONTINUE
    : 'continue'
    ;

FUNCTION
    : 'function'
    ;

RETURN
    : 'return'
    ;

NULL
    : 'null'
    ;

FLOAT
    : IntPart? Fraction
    | IntPart '.'
    ;

INT
    : Digit+
    ;

BOOL
    : 'true'
    | 'false'
    ;

STRING
    : '"' StringCharacters? '"'
    | '\'' StringCharacters? '\''
    ;

IDENTIFIER
    : Letter LetterOrDigit*
    ;

fragment IntPart
    : Digit+
    ;

fragment Fraction
    : '.' Digit+
    ;

fragment Digit
    : [0-9]
    ;

fragment
StringCharacters
    : StringCharacter+
    ;

fragment
StringCharacter
    : ~['"\\\r\n]
    | EscapeSequence
    ;

fragment
EscapeSequence
    : '\\' [btnfr"'\\]
    ;

fragment
Letter
    : [a-zA-Z]
    | '_'
    | '\u0100'..'\u{1FFFF}'
    ;

fragment
LetterOrDigit
    : [a-zA-Z]
    | '_'
    | '\u0100'..'\u{1FFFF}'
    | [0-9]
    ;

SPACE:
    [ \t\n\r]+
    -> skip;

COMMENT:
    (
        ('//' | '#') ~('\r' | '\n')* 
        |
        '/*' .*? '*/'
    )
    -> skip
    ;


