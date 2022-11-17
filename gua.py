#!/usr/bin/env python3

from GuaLexer import GuaLexer
from GuaParser import GuaParser
from GuaVisitor import GuaVisitor


def log(*args):
    print(*args, flush=True)


def string_with_space(num: int, string: str) -> str:
    return num * '    ' + string


class EvalVisitor(GuaVisitor):
    def __init__(self):
        self.num = -1

    def visitBlock(self, ctx: GuaParser.BlockContext):
        self.num += 1

        r = ''

        statements_visit_result = []
        for s in ctx.statement():
            statements_visit_result.append(self.visit(s))

        for m in statements_visit_result:
            r += m

        return_statement = ctx.returnStatement()
        if return_statement is None:
            # TODO 从这里看，go 的 defer 有价值
            self.num -= 1
            return f'{r}'

        return_statement_visit_result = self.visit(return_statement)
        r += return_statement_visit_result

        self.num -= 1
        return f'{r}'

    def visitLabelStatementDefinition(self, ctx: GuaParser.LabelStatementDefinitionContext):
        k = ctx.IDENTIFIER().getText()
        v = self.visit(ctx.expression())

        return string_with_space(self.num, f'var {k} = {v}\n')

    def visitLabelStatementConst(self, ctx: GuaParser.LabelStatementConstContext):
        k = ctx.IDENTIFIER().getText()
        v = self.visit(ctx.expression())

        return string_with_space(self.num, f'con {k} = {v}\n')

    def visitLabelStatementThisDefinition(self, ctx: GuaParser.LabelStatementThisDefinitionContext):
        k = ctx.IDENTIFIER().getText()
        v = self.visit(ctx.expression())

        return string_with_space(self.num, f'var this.{k} = {v}\n')

    def visitLabelStatementThisConst(self, ctx: GuaParser.LabelStatementThisConstContext):
        k = ctx.IDENTIFIER().getText()
        v = self.visit(ctx.expression())

        return string_with_space(self.num, f'con this.{k} = {v}\n')

    def visitLabelStatementClassDefinition(self, ctx: GuaParser.LabelStatementClassDefinitionContext):
        k = ctx.IDENTIFIER().getText()
        v = self.visit(ctx.expression())

        return string_with_space(self.num, f'var class.{k} = {v}\n')

    def visitLabelStatementClassConst(self, ctx: GuaParser.LabelStatementClassConstContext):
        k = ctx.IDENTIFIER().getText()
        v = self.visit(ctx.expression())

        return string_with_space(self.num, f'con class.{k} = {v}\n')

    def visitLabelStatementWhile(self, ctx: GuaParser.LabelStatementWhileContext):
        check = self.visit(ctx.expression())
        block = self.visit(ctx.block())

        result = string_with_space(self.num, f'while ({check}) {{\n')
        result += block
        result += string_with_space(self.num, f'}}\n')

        return result

    def visitLabelStatementBreak(self, ctx: GuaParser.LabelStatementBreakContext):
        return string_with_space(self.num, f'break\n')

    def visitLabelStatementContinue(self, ctx: GuaParser.LabelStatementContinueContext):
        return string_with_space(self.num, f'continue\n')

    def visitLabelStatementIf(self, ctx: GuaParser.LabelStatementIfContext):
        check = self.visit(ctx.expression())
        block = self.visit(ctx.block())

        result = string_with_space(self.num, f'if ({check}) {{\n')
        result += block
        result += string_with_space(self.num, f'}}\n')

        return result

    def visitLabelStatementIfElse(self, ctx: GuaParser.LabelStatementIfElseContext):
        check = self.visit(ctx.expression())
        if_block = self.visit(ctx.block(0))
        else_block = self.visit(ctx.block(1))

        result = string_with_space(self.num, f'if ({check}) {{\n')
        result += if_block
        result += string_with_space(self.num, f'}} else {{\n')
        result += else_block
        result += string_with_space(self.num, f'}}\n')

        return result

    def visitLabelStatementIfElseIf(self, ctx: GuaParser.LabelStatementIfElseIfContext):
        check = self.visit(ctx.expression())
        block = self.visit(ctx.block())
        else_if_blocks = [self.visit(c) for c in ctx.elseIfClause()]

        result = string_with_space(self.num, f'if ({check}) {{\n')
        result += block
        for b in else_if_blocks:
            result += b
        result += string_with_space(self.num, f'}}\n')

        return result

    def visitLabelStatementIfElseIfElse(self, ctx: GuaParser.LabelStatementIfElseIfElseContext):
        check = self.visit(ctx.expression())
        if_block = self.visit(ctx.block(0))
        else_if_blocks = [self.visit(c) for c in ctx.elseIfClause()]
        else_block = self.visit(ctx.block(1))

        result = string_with_space(self.num, f'if ({check}) {{\n')
        result += if_block
        for b in else_if_blocks:
            result += b
        result += string_with_space(self.num, f'}} else {{\n')
        result += else_block
        result += string_with_space(self.num, f'}}\n')

        return result

    def visitLabelStatementFor(self, ctx: GuaParser.LabelStatementForContext):
        init = self.visit(ctx.forInitClause())
        compare = self.visit(ctx.expression())
        assign = self.visit(ctx.forAssignClause())
        block = self.visit(ctx.block())

        result = string_with_space(self.num, f'for ({init}; {compare}; {assign}) {{\n')
        result += block
        result += string_with_space(self.num, f'}}\n')

        return result

    def visitLabelStatementAssignVar(self, ctx: GuaParser.LabelStatementAssignVarContext):
        k = ctx.IDENTIFIER().getText()
        op = ctx.op.text
        v = self.visit(ctx.expression())
        return string_with_space(self.num, f'{k} {op} {v}\n')

    def visitLabelStatementAssignThisField(self, ctx: GuaParser.LabelStatementAssignThisFieldContext):
        field = ctx.IDENTIFIER().getText()
        op = ctx.op.text
        value = self.visit(ctx.expression())
        return string_with_space(self.num, f'this.{field} {op} {value}\n')

    def visitLabelStatementAssignClassField(self, ctx: GuaParser.LabelStatementAssignClassFieldContext):
        field = ctx.IDENTIFIER().getText()
        op = ctx.op.text
        value = self.visit(ctx.expression())
        return string_with_space(self.num, f'class.{field} {op} {value}\n')

    def visitLabelStatementAssignField(self, ctx: GuaParser.LabelStatementAssignFieldContext):
        name = ctx.IDENTIFIER(0).getText()
        field = ctx.IDENTIFIER(1).getText()
        op = ctx.op.text
        value = self.visit(ctx.expression())
        return string_with_space(self.num, f'{name}.{field} {op} {value}\n')

    def visitLabelStatementFunction(self, ctx: GuaParser.LabelStatementFunctionContext):
        name = ctx.IDENTIFIER().getText()
        parameter = self.visit(ctx.formalParameters())
        block = self.visit(ctx.block())

        result = string_with_space(self.num, f'con {name} = function({parameter}) {{\n')
        result += block
        result += string_with_space(self.num, f'}}\n')

        return result

    def visitLabelStatementClass(self, ctx: GuaParser.LabelStatementClassContext):
        name = ctx.IDENTIFIER().getText()
        parameter = self.visit(ctx.formalParameters())
        block = self.visit(ctx.block())

        result = string_with_space(self.num, f'con {name} = class({parameter}) {{\n')
        result += block
        result += string_with_space(self.num, f'}}\n')

        return result

    def visitLabelStatementClassFunction(self, ctx: GuaParser.LabelStatementClassFunctionContext):
        name = ctx.IDENTIFIER().getText()
        parameter = self.visit(ctx.formalParameters())
        block = self.visit(ctx.block())

        result = string_with_space(self.num, f'con class.{name} = function({parameter}) {{\n')
        result += block
        result += string_with_space(self.num, f'}}\n')

        return result

    def visitLabelStatementFunctionCall(self, ctx: GuaParser.LabelStatementFunctionCallContext):
        r = self.visit(ctx.functionCallItem())
        return string_with_space(self.num, f'{r}\n')

    def visitLabelStatementFunctionCallChain(self, ctx: GuaParser.LabelStatementFunctionCallChainContext):
        fs = [self.visit(s) for s in ctx.clainItem()]
        return string_with_space(self.num, '.'.join(fs) + '\n')

    def visitLabelStatementMethodCall(self, ctx: GuaParser.LabelStatementMethodCallContext):
        r = self.visit(ctx.methodCallItem())
        return string_with_space(self.num, f'{r}\n')

    def visitLabelStatementMethodCallChain(self, ctx: GuaParser.LabelStatementMethodCallChainContext):
        m = self.visit(ctx.methodCallItem())
        fs = [self.visit(s) for s in ctx.clainItem()]
        return string_with_space(self.num, m + '.' + '.'.join(fs) + '\n')

    def visitReturnStatement(self, ctx: GuaParser.ReturnStatementContext):
        v = self.visit(ctx.expression())
        return string_with_space(self.num, f'return {v}\n')

    def visitElseIfClause(self, ctx: GuaParser.ElseIfClauseContext):
        check = self.visit(ctx.expression())
        block = self.visit(ctx.block())

        result = string_with_space(self.num, f'}} else if {check} {{\n')
        result += block

        return result

    def visitForInitClause(self, ctx: GuaParser.ForInitClauseContext):
        k = ctx.IDENTIFIER().getText()
        v = self.visit(ctx.expression())
        return f'var {k} = {v}'

    def visitForAssignClause(self, ctx: GuaParser.ForAssignClauseContext):
        a = ctx.IDENTIFIER().getText()
        op = ctx.op.text
        b = self.visit(ctx.expression())
        return f'{a} {op} {b}'

    def visitFormalParameters(self, ctx: GuaParser.FormalParametersContext):
        ts = []
        for t in ctx.IDENTIFIER():
            ts.append(t.getText())
        return ', '.join(ts)

    def visitActualParameters(self, ctx: GuaParser.ActualParametersContext):
        es = [self.visit(s) for s in ctx.expression()]
        return ', '.join(es)

    def visitLabelExpressionMulDivMod(self, ctx: GuaParser.LabelExpressionMulDivModContext):
        op = ctx.op.text
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return f'{a} {op} {b}'

    def visitLabelExpressionAddSub(self, ctx: GuaParser.LabelExpressionAddSubContext):
        op = ctx.op.text
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return f'{a} {op} {b}'

    def visitLabelExpressionBitMove(self, ctx: GuaParser.LabelExpressionBitMoveContext):
        op = ctx.op.text
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return f'{a} {op} {b}'

    def visitLabelExpressionBitAnd(self, ctx: GuaParser.LabelExpressionBitAndContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return f'{a} & {b}'

    def visitLabelExpressionBitNot(self, ctx: GuaParser.LabelExpressionBitNotContext):
        a = self.visit(ctx.expression())
        return f'~{a}'

    def visitLabelExpressionBitOr(self, ctx: GuaParser.LabelExpressionBitOrContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return f'{a} | {b}'

    def visitLabelExpressionRelation(self, ctx: GuaParser.LabelExpressionRelationContext):
        op = ctx.op.text
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return f'{a} {op} {b}'

    def visitLabelExpressionAnd(self, ctx: GuaParser.LabelExpressionAndContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return f'{a} and {b}'

    def visitLabelExpressionOr(self, ctx: GuaParser.LabelExpressionOrContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return f'{a} or {b}'

    def visitLabelExpressionThisFieldCall(self, ctx: GuaParser.LabelExpressionThisFieldCallContext):
        r = ctx.IDENTIFIER().getText()
        return f'this.{r}'

    def visitLabelExpressionThisFieldCallChain(self, ctx: GuaParser.LabelExpressionThisFieldCallChainContext):
        m = ctx.IDENTIFIER().getText()
        fs = [self.visit(s) for s in ctx.clainItem()]
        return 'this.' + m + '.' + '.'.join(fs)

    def visitLabelExpressionClassFieldCall(self, ctx: GuaParser.LabelExpressionClassFieldCallContext):
        r = ctx.IDENTIFIER().getText()
        return f'class.{r}'

    def visitLabelExpressionClassFieldCallChain(self, ctx: GuaParser.LabelExpressionClassFieldCallChainContext):
        m = ctx.IDENTIFIER().getText()
        fs = [self.visit(s) for s in ctx.clainItem()]
        return 'class.' + m + '.' + '.'.join(fs)

    def visitLabelExpressionFieldCall(self, ctx: GuaParser.LabelExpressionFieldCallContext):
        ms = [s.getText() for s in ctx.IDENTIFIER()]
        return '.'.join(ms)

    def visitLabelExpressionFieldCallChain(self, ctx: GuaParser.LabelExpressionFieldCallChainContext):
        m = ctx.IDENTIFIER().getText()
        fs = [self.visit(s) for s in ctx.clainItem()]
        return m + '.' + '.'.join(fs)

    def visitLabelExpressionFunctionCall(self, ctx: GuaParser.LabelExpressionFunctionCallContext):
        r = self.visit(ctx.functionCallItem())
        return f'{r}'

    def visitLabelExpressionFunctionCallChain(self, ctx: GuaParser.LabelExpressionFunctionCallChainContext):
        m = self.visit(ctx.functionCallItem())
        fs = [self.visit(s) for s in ctx.clainItem()]
        return m + '.' + '.'.join(fs)

    def visitLabelExpressionMethodCall(self, ctx: GuaParser.LabelExpressionMethodCallContext):
        r = self.visit(ctx.methodCallItem())
        return f'{r}'

    def visitLabelExpressionMethodCallChain(self, ctx: GuaParser.LabelExpressionMethodCallChainContext):
        m = self.visit(ctx.methodCallItem())
        fs = [self.visit(s) for s in ctx.clainItem()]
        return m + '.' + '.'.join(fs)

    def visitLabelExpressionArray(self, ctx: GuaParser.LabelExpressionArrayContext):
        es = [self.visit(s) for s in ctx.expression()]
        return '[' + ', '.join(es) + ']'

    def visitLabelExpressionMap(self, ctx: GuaParser.LabelExpressionMapContext):
        es = [self.visit(s) for s in ctx.mapItem()]
        return '{' + ', '.join(es) + '}'

    def visitMapItem(self, ctx: GuaParser.MapItemContext):
        a = ctx.STRING().getText()
        b = self.visit(ctx.expression())
        return f'{a}: {b}'

    def visitFunctionCallItem(self, ctx: GuaParser.FunctionCallItemContext):
        name = ctx.IDENTIFIER().getText()
        parameter = self.visit(ctx.actualParameters())
        return f'{name}({parameter})'

    def visitMethodCallItem(self, ctx: GuaParser.MethodCallItemContext):
        name = ctx.IDENTIFIER(0).getText()
        function = ctx.IDENTIFIER(1).getText()
        parameter = self.visit(ctx.actualParameters())
        return f'{name}.{function}({parameter})'

    def visitClainItem(self, ctx: GuaParser.ClainItemContext):
        if ctx.functionCallItem() is None:
            return f'{ctx.IDENTIFIER().getText()}'
        else:
            return f'{self.visit(ctx.functionCallItem())}'

    def visitLabelExpressionLiteralNull(self, ctx: GuaParser.LabelExpressionLiteralNullContext):
        r = ctx.NULL().getText()
        return f'{r}'

    def visitLabelExpressionLiteralFloat(self, ctx: GuaParser.LabelExpressionLiteralFloatContext):
        r = ctx.FLOAT().getText()
        return f'{r}'

    def visitLabelExpressionLiteralInt(self, ctx):
        r = ctx.INT().getText()
        return f'{r}'

    def visitLabelExpressionLiteralBool(self, ctx: GuaParser.LabelExpressionLiteralBoolContext):
        r = ctx.BOOL().getText()
        return f'{r}'

    def visitLabelExpressionLiteralString(self, ctx: GuaParser.LabelExpressionLiteralStringContext):
        r = ctx.STRING().getText()
        return f'{r}'

    def visitLabelExpressionIdentifier(self, ctx: GuaParser.LabelExpressionIdentifierContext):
        r = ctx.IDENTIFIER().getText()
        return f'{r}'


def main():
    import antlr4 as ant
    # 写死了读取 main.gua
    path = 'main.gua'
    fs = ant.FileStream(path, encoding='utf-8')
    lexer = GuaLexer(fs)
    tokens = ant.CommonTokenStream(lexer)
    ast = GuaParser(tokens).block()
    visitor = EvalVisitor()
    output = visitor.visit(ast)
    log(output)


if __name__ == '__main__':
    main()
