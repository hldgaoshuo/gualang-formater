# Generated from Gua.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GuaParser import GuaParser
else:
    from GuaParser import GuaParser

# This class defines a complete generic visitor for a parse tree produced by GuaParser.

class GuaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GuaParser#block.
    def visitBlock(self, ctx:GuaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementDefinition.
    def visitLabelStatementDefinition(self, ctx:GuaParser.LabelStatementDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementConst.
    def visitLabelStatementConst(self, ctx:GuaParser.LabelStatementConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementThisDefinition.
    def visitLabelStatementThisDefinition(self, ctx:GuaParser.LabelStatementThisDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementThisConst.
    def visitLabelStatementThisConst(self, ctx:GuaParser.LabelStatementThisConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementClassDefinition.
    def visitLabelStatementClassDefinition(self, ctx:GuaParser.LabelStatementClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementClassConst.
    def visitLabelStatementClassConst(self, ctx:GuaParser.LabelStatementClassConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementWhile.
    def visitLabelStatementWhile(self, ctx:GuaParser.LabelStatementWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementBreak.
    def visitLabelStatementBreak(self, ctx:GuaParser.LabelStatementBreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementContinue.
    def visitLabelStatementContinue(self, ctx:GuaParser.LabelStatementContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementIf.
    def visitLabelStatementIf(self, ctx:GuaParser.LabelStatementIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementIfElse.
    def visitLabelStatementIfElse(self, ctx:GuaParser.LabelStatementIfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementIfElseIf.
    def visitLabelStatementIfElseIf(self, ctx:GuaParser.LabelStatementIfElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementIfElseIfElse.
    def visitLabelStatementIfElseIfElse(self, ctx:GuaParser.LabelStatementIfElseIfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementFor.
    def visitLabelStatementFor(self, ctx:GuaParser.LabelStatementForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementAssignVar.
    def visitLabelStatementAssignVar(self, ctx:GuaParser.LabelStatementAssignVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementAssignThisField.
    def visitLabelStatementAssignThisField(self, ctx:GuaParser.LabelStatementAssignThisFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementAssignClassField.
    def visitLabelStatementAssignClassField(self, ctx:GuaParser.LabelStatementAssignClassFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementAssignField.
    def visitLabelStatementAssignField(self, ctx:GuaParser.LabelStatementAssignFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementFunction.
    def visitLabelStatementFunction(self, ctx:GuaParser.LabelStatementFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementClass.
    def visitLabelStatementClass(self, ctx:GuaParser.LabelStatementClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementClassFunction.
    def visitLabelStatementClassFunction(self, ctx:GuaParser.LabelStatementClassFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementFunctionCall.
    def visitLabelStatementFunctionCall(self, ctx:GuaParser.LabelStatementFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementFunctionCallChain.
    def visitLabelStatementFunctionCallChain(self, ctx:GuaParser.LabelStatementFunctionCallChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementMethodCall.
    def visitLabelStatementMethodCall(self, ctx:GuaParser.LabelStatementMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelStatementMethodCallChain.
    def visitLabelStatementMethodCallChain(self, ctx:GuaParser.LabelStatementMethodCallChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#returnStatement.
    def visitReturnStatement(self, ctx:GuaParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#elseIfClause.
    def visitElseIfClause(self, ctx:GuaParser.ElseIfClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#forInitClause.
    def visitForInitClause(self, ctx:GuaParser.ForInitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#forAssignClause.
    def visitForAssignClause(self, ctx:GuaParser.ForAssignClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionArray.
    def visitLabelExpressionArray(self, ctx:GuaParser.LabelExpressionArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionRelation.
    def visitLabelExpressionRelation(self, ctx:GuaParser.LabelExpressionRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionFunctionCallChain.
    def visitLabelExpressionFunctionCallChain(self, ctx:GuaParser.LabelExpressionFunctionCallChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionClassFieldCallChain.
    def visitLabelExpressionClassFieldCallChain(self, ctx:GuaParser.LabelExpressionClassFieldCallChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionAddSub.
    def visitLabelExpressionAddSub(self, ctx:GuaParser.LabelExpressionAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionFieldCall.
    def visitLabelExpressionFieldCall(self, ctx:GuaParser.LabelExpressionFieldCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionLiteralNull.
    def visitLabelExpressionLiteralNull(self, ctx:GuaParser.LabelExpressionLiteralNullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionLiteralInt.
    def visitLabelExpressionLiteralInt(self, ctx:GuaParser.LabelExpressionLiteralIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionBitOr.
    def visitLabelExpressionBitOr(self, ctx:GuaParser.LabelExpressionBitOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionMethodCallChain.
    def visitLabelExpressionMethodCallChain(self, ctx:GuaParser.LabelExpressionMethodCallChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionMulDivMod.
    def visitLabelExpressionMulDivMod(self, ctx:GuaParser.LabelExpressionMulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionThisFieldCall.
    def visitLabelExpressionThisFieldCall(self, ctx:GuaParser.LabelExpressionThisFieldCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionIdentifier.
    def visitLabelExpressionIdentifier(self, ctx:GuaParser.LabelExpressionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionFunctionCall.
    def visitLabelExpressionFunctionCall(self, ctx:GuaParser.LabelExpressionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionLiteralString.
    def visitLabelExpressionLiteralString(self, ctx:GuaParser.LabelExpressionLiteralStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionAnd.
    def visitLabelExpressionAnd(self, ctx:GuaParser.LabelExpressionAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionClassFieldCall.
    def visitLabelExpressionClassFieldCall(self, ctx:GuaParser.LabelExpressionClassFieldCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionThisFieldCallChain.
    def visitLabelExpressionThisFieldCallChain(self, ctx:GuaParser.LabelExpressionThisFieldCallChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionMethodCall.
    def visitLabelExpressionMethodCall(self, ctx:GuaParser.LabelExpressionMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionOr.
    def visitLabelExpressionOr(self, ctx:GuaParser.LabelExpressionOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionBitMove.
    def visitLabelExpressionBitMove(self, ctx:GuaParser.LabelExpressionBitMoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionBitAnd.
    def visitLabelExpressionBitAnd(self, ctx:GuaParser.LabelExpressionBitAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionBitNot.
    def visitLabelExpressionBitNot(self, ctx:GuaParser.LabelExpressionBitNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionLiteralFloat.
    def visitLabelExpressionLiteralFloat(self, ctx:GuaParser.LabelExpressionLiteralFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionFieldCallChain.
    def visitLabelExpressionFieldCallChain(self, ctx:GuaParser.LabelExpressionFieldCallChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionMap.
    def visitLabelExpressionMap(self, ctx:GuaParser.LabelExpressionMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#LabelExpressionLiteralBool.
    def visitLabelExpressionLiteralBool(self, ctx:GuaParser.LabelExpressionLiteralBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#mapItem.
    def visitMapItem(self, ctx:GuaParser.MapItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#functionCallItem.
    def visitFunctionCallItem(self, ctx:GuaParser.FunctionCallItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#methodCallItem.
    def visitMethodCallItem(self, ctx:GuaParser.MethodCallItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#clainItem.
    def visitClainItem(self, ctx:GuaParser.ClainItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#formalParameters.
    def visitFormalParameters(self, ctx:GuaParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GuaParser#actualParameters.
    def visitActualParameters(self, ctx:GuaParser.ActualParametersContext):
        return self.visitChildren(ctx)



del GuaParser