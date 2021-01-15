# Generated from C.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

## @file
# The file defines the parser for C source files.
#
# THIS FILE IS AUTO-GENENERATED. PLEASE DON NOT MODIFY THIS FILE.
# This file is generated by running:
# java org.antlr.Tool C.g
#
# Copyright (c) 2009 - 2010, Intel Corporation  All rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause-Patent
#
##

import edk2basetools.Ecc.CodeFragment as CodeFragment
import edk2basetools.Ecc.FileProfile as FileProfile


# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#translation_unit.
    # @param  ctx Type: CParser.Translation_unitContext
    def enterTranslation_unit(self,ctx):
        pass

    # Exit a parse tree produced by CParser#translation_unit.
    # @param  ctx Type: CParser.Translation_unitContext
    def exitTranslation_unit(self,ctx):
        pass


    # Enter a parse tree produced by CParser#external_declaration.
    # @param  ctx Type: CParser.External_declarationContext
    def enterExternal_declaration(self,ctx):
        pass

    # Exit a parse tree produced by CParser#external_declaration.
    # @param  ctx Type: CParser.External_declarationContext
    def exitExternal_declaration(self,ctx):
        pass


    # Enter a parse tree produced by CParser#function_definition.
    # @param  ctx Type: CParser.Function_definitionContext
    def enterFunction_definition(self,ctx):
        pass

    # Exit a parse tree produced by CParser#function_definition.
    # @param  ctx Type: CParser.Function_definitionContext
    def exitFunction_definition(self,ctx):
        pass


    # Enter a parse tree produced by CParser#declaration_specifiers.
    # @param  ctx Type: CParser.Declaration_specifiersContext
    def enterDeclaration_specifiers(self,ctx):
        pass

    # Exit a parse tree produced by CParser#declaration_specifiers.
    # @param  ctx Type: CParser.Declaration_specifiersContext
    def exitDeclaration_specifiers(self,ctx):
        pass


    # Enter a parse tree produced by CParser#declaration.
    # @param  ctx Type: CParser.DeclarationContext
    def enterDeclaration(self,ctx):
        pass

    # Exit a parse tree produced by CParser#declaration.
    # @param  ctx Type: CParser.DeclarationContext
    def exitDeclaration(self,ctx):
        pass


    # Enter a parse tree produced by CParser#init_declarator_list.
    # @param  ctx Type: CParser.Init_declarator_listContext
    def enterInit_declarator_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#init_declarator_list.
    # @param  ctx Type: CParser.Init_declarator_listContext
    def exitInit_declarator_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#init_declarator.
    # @param  ctx Type: CParser.Init_declaratorContext
    def enterInit_declarator(self,ctx):
        pass

    # Exit a parse tree produced by CParser#init_declarator.
    # @param  ctx Type: CParser.Init_declaratorContext
    def exitInit_declarator(self,ctx):
        pass


    # Enter a parse tree produced by CParser#storage_class_specifier.
    # @param  ctx Type: CParser.Storage_class_specifierContext
    def enterStorage_class_specifier(self,ctx):
        pass

    # Exit a parse tree produced by CParser#storage_class_specifier.
    # @param  ctx Type: CParser.Storage_class_specifierContext
    def exitStorage_class_specifier(self,ctx):
        pass


    # Enter a parse tree produced by CParser#type_specifier.
    # @param  ctx Type: CParser.Type_specifierContext
    def enterType_specifier(self,ctx):
        pass

    # Exit a parse tree produced by CParser#type_specifier.
    # @param  ctx Type: CParser.Type_specifierContext
    def exitType_specifier(self,ctx):
        pass


    # Enter a parse tree produced by CParser#type_id.
    # @param  ctx Type: CParser.Type_idContext
    def enterType_id(self,ctx):
        pass

    # Exit a parse tree produced by CParser#type_id.
    # @param  ctx Type: CParser.Type_idContext
    def exitType_id(self,ctx):
        pass


    # Enter a parse tree produced by CParser#struct_or_union_specifier.
    # @param  ctx Type: CParser.Struct_or_union_specifierContext
    def enterStruct_or_union_specifier(self,ctx):
        pass

    # Exit a parse tree produced by CParser#struct_or_union_specifier.
    # @param  ctx Type: CParser.Struct_or_union_specifierContext
    def exitStruct_or_union_specifier(self,ctx):
        pass


    # Enter a parse tree produced by CParser#struct_or_union.
    # @param  ctx Type: CParser.Struct_or_unionContext
    def enterStruct_or_union(self,ctx):
        pass

    # Exit a parse tree produced by CParser#struct_or_union.
    # @param  ctx Type: CParser.Struct_or_unionContext
    def exitStruct_or_union(self,ctx):
        pass


    # Enter a parse tree produced by CParser#struct_declaration_list.
    # @param  ctx Type: CParser.Struct_declaration_listContext
    def enterStruct_declaration_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#struct_declaration_list.
    # @param  ctx Type: CParser.Struct_declaration_listContext
    def exitStruct_declaration_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#struct_declaration.
    # @param  ctx Type: CParser.Struct_declarationContext
    def enterStruct_declaration(self,ctx):
        pass

    # Exit a parse tree produced by CParser#struct_declaration.
    # @param  ctx Type: CParser.Struct_declarationContext
    def exitStruct_declaration(self,ctx):
        pass


    # Enter a parse tree produced by CParser#specifier_qualifier_list.
    # @param  ctx Type: CParser.Specifier_qualifier_listContext
    def enterSpecifier_qualifier_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#specifier_qualifier_list.
    # @param  ctx Type: CParser.Specifier_qualifier_listContext
    def exitSpecifier_qualifier_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#struct_declarator_list.
    # @param  ctx Type: CParser.Struct_declarator_listContext
    def enterStruct_declarator_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#struct_declarator_list.
    # @param  ctx Type: CParser.Struct_declarator_listContext
    def exitStruct_declarator_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#struct_declarator.
    # @param  ctx Type: CParser.Struct_declaratorContext
    def enterStruct_declarator(self,ctx):
        pass

    # Exit a parse tree produced by CParser#struct_declarator.
    # @param  ctx Type: CParser.Struct_declaratorContext
    def exitStruct_declarator(self,ctx):
        pass


    # Enter a parse tree produced by CParser#enum_specifier.
    # @param  ctx Type: CParser.Enum_specifierContext
    def enterEnum_specifier(self,ctx):
        pass

    # Exit a parse tree produced by CParser#enum_specifier.
    # @param  ctx Type: CParser.Enum_specifierContext
    def exitEnum_specifier(self,ctx):
        pass


    # Enter a parse tree produced by CParser#enumerator_list.
    # @param  ctx Type: CParser.Enumerator_listContext
    def enterEnumerator_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#enumerator_list.
    # @param  ctx Type: CParser.Enumerator_listContext
    def exitEnumerator_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#enumerator.
    # @param  ctx Type: CParser.EnumeratorContext
    def enterEnumerator(self,ctx):
        pass

    # Exit a parse tree produced by CParser#enumerator.
    # @param  ctx Type: CParser.EnumeratorContext
    def exitEnumerator(self,ctx):
        pass


    # Enter a parse tree produced by CParser#type_qualifier.
    # @param  ctx Type: CParser.Type_qualifierContext
    def enterType_qualifier(self,ctx):
        pass

    # Exit a parse tree produced by CParser#type_qualifier.
    # @param  ctx Type: CParser.Type_qualifierContext
    def exitType_qualifier(self,ctx):
        pass


    # Enter a parse tree produced by CParser#declarator.
    # @param  ctx Type: CParser.DeclaratorContext
    def enterDeclarator(self,ctx):
        pass

    # Exit a parse tree produced by CParser#declarator.
    # @param  ctx Type: CParser.DeclaratorContext
    def exitDeclarator(self,ctx):
        pass


    # Enter a parse tree produced by CParser#direct_declarator.
    # @param  ctx Type: CParser.Direct_declaratorContext
    def enterDirect_declarator(self,ctx):
        pass

    # Exit a parse tree produced by CParser#direct_declarator.
    # @param  ctx Type: CParser.Direct_declaratorContext
    def exitDirect_declarator(self,ctx):
        pass


    # Enter a parse tree produced by CParser#declarator_suffix.
    # @param  ctx Type: CParser.Declarator_suffixContext
    def enterDeclarator_suffix(self,ctx):
        pass

    # Exit a parse tree produced by CParser#declarator_suffix.
    # @param  ctx Type: CParser.Declarator_suffixContext
    def exitDeclarator_suffix(self,ctx):
        pass


    # Enter a parse tree produced by CParser#pointer.
    # @param  ctx Type: CParser.PointerContext
    def enterPointer(self,ctx):
        pass

    # Exit a parse tree produced by CParser#pointer.
    # @param  ctx Type: CParser.PointerContext
    def exitPointer(self,ctx):
        pass


    # Enter a parse tree produced by CParser#parameter_type_list.
    # @param  ctx Type: CParser.Parameter_type_listContext
    def enterParameter_type_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#parameter_type_list.
    # @param  ctx Type: CParser.Parameter_type_listContext
    def exitParameter_type_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#parameter_list.
    # @param  ctx Type: CParser.Parameter_listContext
    def enterParameter_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#parameter_list.
    # @param  ctx Type: CParser.Parameter_listContext
    def exitParameter_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#parameter_declaration.
    # @param  ctx Type: CParser.Parameter_declarationContext
    def enterParameter_declaration(self,ctx):
        pass

    # Exit a parse tree produced by CParser#parameter_declaration.
    # @param  ctx Type: CParser.Parameter_declarationContext
    def exitParameter_declaration(self,ctx):
        pass


    # Enter a parse tree produced by CParser#identifier_list.
    # @param  ctx Type: CParser.Identifier_listContext
    def enterIdentifier_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#identifier_list.
    # @param  ctx Type: CParser.Identifier_listContext
    def exitIdentifier_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#type_name.
    # @param  ctx Type: CParser.Type_nameContext
    def enterType_name(self,ctx):
        pass

    # Exit a parse tree produced by CParser#type_name.
    # @param  ctx Type: CParser.Type_nameContext
    def exitType_name(self,ctx):
        pass


    # Enter a parse tree produced by CParser#abstract_declarator.
    # @param  ctx Type: CParser.Abstract_declaratorContext
    def enterAbstract_declarator(self,ctx):
        pass

    # Exit a parse tree produced by CParser#abstract_declarator.
    # @param  ctx Type: CParser.Abstract_declaratorContext
    def exitAbstract_declarator(self,ctx):
        pass


    # Enter a parse tree produced by CParser#direct_abstract_declarator.
    # @param  ctx Type: CParser.Direct_abstract_declaratorContext
    def enterDirect_abstract_declarator(self,ctx):
        pass

    # Exit a parse tree produced by CParser#direct_abstract_declarator.
    # @param  ctx Type: CParser.Direct_abstract_declaratorContext
    def exitDirect_abstract_declarator(self,ctx):
        pass


    # Enter a parse tree produced by CParser#abstract_declarator_suffix.
    # @param  ctx Type: CParser.Abstract_declarator_suffixContext
    def enterAbstract_declarator_suffix(self,ctx):
        pass

    # Exit a parse tree produced by CParser#abstract_declarator_suffix.
    # @param  ctx Type: CParser.Abstract_declarator_suffixContext
    def exitAbstract_declarator_suffix(self,ctx):
        pass


    # Enter a parse tree produced by CParser#initializer.
    # @param  ctx Type: CParser.InitializerContext
    def enterInitializer(self,ctx):
        pass

    # Exit a parse tree produced by CParser#initializer.
    # @param  ctx Type: CParser.InitializerContext
    def exitInitializer(self,ctx):
        pass


    # Enter a parse tree produced by CParser#initializer_list.
    # @param  ctx Type: CParser.Initializer_listContext
    def enterInitializer_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#initializer_list.
    # @param  ctx Type: CParser.Initializer_listContext
    def exitInitializer_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#argument_expression_list.
    # @param  ctx Type: CParser.Argument_expression_listContext
    def enterArgument_expression_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#argument_expression_list.
    # @param  ctx Type: CParser.Argument_expression_listContext
    def exitArgument_expression_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#additive_expression.
    # @param  ctx Type: CParser.Additive_expressionContext
    def enterAdditive_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#additive_expression.
    # @param  ctx Type: CParser.Additive_expressionContext
    def exitAdditive_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#multiplicative_expression.
    # @param  ctx Type: CParser.Multiplicative_expressionContext
    def enterMultiplicative_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#multiplicative_expression.
    # @param  ctx Type: CParser.Multiplicative_expressionContext
    def exitMultiplicative_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#cast_expression.
    # @param  ctx Type: CParser.Cast_expressionContext
    def enterCast_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#cast_expression.
    # @param  ctx Type: CParser.Cast_expressionContext
    def exitCast_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#unary_expression.
    # @param  ctx Type: CParser.Unary_expressionContext
    def enterUnary_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#unary_expression.
    # @param  ctx Type: CParser.Unary_expressionContext
    def exitUnary_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#postfix_expression.
    # @param  ctx Type: CParser.Postfix_expressionContext
    def enterPostfix_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#postfix_expression.
    # @param  ctx Type: CParser.Postfix_expressionContext
    def exitPostfix_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#macro_parameter_list.
    # @param  ctx Type: CParser.Macro_parameter_listContext
    def enterMacro_parameter_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#macro_parameter_list.
    # @param  ctx Type: CParser.Macro_parameter_listContext
    def exitMacro_parameter_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#unary_operator.
    # @param  ctx Type: CParser.Unary_operatorContext
    def enterUnary_operator(self,ctx):
        pass

    # Exit a parse tree produced by CParser#unary_operator.
    # @param  ctx Type: CParser.Unary_operatorContext
    def exitUnary_operator(self,ctx):
        pass


    # Enter a parse tree produced by CParser#primary_expression.
    # @param  ctx Type: CParser.Primary_expressionContext
    def enterPrimary_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#primary_expression.
    # @param  ctx Type: CParser.Primary_expressionContext
    def exitPrimary_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#constant.
    # @param  ctx Type: CParser.ConstantContext
    def enterConstant(self,ctx):
        pass

    # Exit a parse tree produced by CParser#constant.
    # @param  ctx Type: CParser.ConstantContext
    def exitConstant(self,ctx):
        pass


    # Enter a parse tree produced by CParser#expression.
    # @param  ctx Type: CParser.ExpressionContext
    def enterExpression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#expression.
    # @param  ctx Type: CParser.ExpressionContext
    def exitExpression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#constant_expression.
    # @param  ctx Type: CParser.Constant_expressionContext
    def enterConstant_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#constant_expression.
    # @param  ctx Type: CParser.Constant_expressionContext
    def exitConstant_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#assignment_expression.
    # @param  ctx Type: CParser.Assignment_expressionContext
    def enterAssignment_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#assignment_expression.
    # @param  ctx Type: CParser.Assignment_expressionContext
    def exitAssignment_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#lvalue.
    # @param  ctx Type: CParser.LvalueContext
    def enterLvalue(self,ctx):
        pass

    # Exit a parse tree produced by CParser#lvalue.
    # @param  ctx Type: CParser.LvalueContext
    def exitLvalue(self,ctx):
        pass


    # Enter a parse tree produced by CParser#assignment_operator.
    # @param  ctx Type: CParser.Assignment_operatorContext
    def enterAssignment_operator(self,ctx):
        pass

    # Exit a parse tree produced by CParser#assignment_operator.
    # @param  ctx Type: CParser.Assignment_operatorContext
    def exitAssignment_operator(self,ctx):
        pass


    # Enter a parse tree produced by CParser#conditional_expression.
    # @param  ctx Type: CParser.Conditional_expressionContext
    def enterConditional_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#conditional_expression.
    # @param  ctx Type: CParser.Conditional_expressionContext
    def exitConditional_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#logical_or_expression.
    # @param  ctx Type: CParser.Logical_or_expressionContext
    def enterLogical_or_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#logical_or_expression.
    # @param  ctx Type: CParser.Logical_or_expressionContext
    def exitLogical_or_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#logical_and_expression.
    # @param  ctx Type: CParser.Logical_and_expressionContext
    def enterLogical_and_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#logical_and_expression.
    # @param  ctx Type: CParser.Logical_and_expressionContext
    def exitLogical_and_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#inclusive_or_expression.
    # @param  ctx Type: CParser.Inclusive_or_expressionContext
    def enterInclusive_or_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#inclusive_or_expression.
    # @param  ctx Type: CParser.Inclusive_or_expressionContext
    def exitInclusive_or_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#exclusive_or_expression.
    # @param  ctx Type: CParser.Exclusive_or_expressionContext
    def enterExclusive_or_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#exclusive_or_expression.
    # @param  ctx Type: CParser.Exclusive_or_expressionContext
    def exitExclusive_or_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#and_expression.
    # @param  ctx Type: CParser.And_expressionContext
    def enterAnd_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#and_expression.
    # @param  ctx Type: CParser.And_expressionContext
    def exitAnd_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#equality_expression.
    # @param  ctx Type: CParser.Equality_expressionContext
    def enterEquality_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#equality_expression.
    # @param  ctx Type: CParser.Equality_expressionContext
    def exitEquality_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#relational_expression.
    # @param  ctx Type: CParser.Relational_expressionContext
    def enterRelational_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#relational_expression.
    # @param  ctx Type: CParser.Relational_expressionContext
    def exitRelational_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#shift_expression.
    # @param  ctx Type: CParser.Shift_expressionContext
    def enterShift_expression(self,ctx):
        pass

    # Exit a parse tree produced by CParser#shift_expression.
    # @param  ctx Type: CParser.Shift_expressionContext
    def exitShift_expression(self,ctx):
        pass


    # Enter a parse tree produced by CParser#statement.
    # @param  ctx Type: CParser.StatementContext
    def enterStatement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#statement.
    # @param  ctx Type: CParser.StatementContext
    def exitStatement(self,ctx):
        pass


    # Enter a parse tree produced by CParser#asm2_statement.
    # @param  ctx Type: CParser.Asm2_statementContext
    def enterAsm2_statement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#asm2_statement.
    # @param  ctx Type: CParser.Asm2_statementContext
    def exitAsm2_statement(self,ctx):
        pass


    # Enter a parse tree produced by CParser#asm1_statement.
    # @param  ctx Type: CParser.Asm1_statementContext
    def enterAsm1_statement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#asm1_statement.
    # @param  ctx Type: CParser.Asm1_statementContext
    def exitAsm1_statement(self,ctx):
        pass


    # Enter a parse tree produced by CParser#asm_statement.
    # @param  ctx Type: CParser.Asm_statementContext
    def enterAsm_statement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#asm_statement.
    # @param  ctx Type: CParser.Asm_statementContext
    def exitAsm_statement(self,ctx):
        pass


    # Enter a parse tree produced by CParser#macro_statement.
    # @param  ctx Type: CParser.Macro_statementContext
    def enterMacro_statement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#macro_statement.
    # @param  ctx Type: CParser.Macro_statementContext
    def exitMacro_statement(self,ctx):
        pass


    # Enter a parse tree produced by CParser#labeled_statement.
    # @param  ctx Type: CParser.Labeled_statementContext
    def enterLabeled_statement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#labeled_statement.
    # @param  ctx Type: CParser.Labeled_statementContext
    def exitLabeled_statement(self,ctx):
        pass


    # Enter a parse tree produced by CParser#compound_statement.
    # @param  ctx Type: CParser.Compound_statementContext
    def enterCompound_statement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#compound_statement.
    # @param  ctx Type: CParser.Compound_statementContext
    def exitCompound_statement(self,ctx):
        pass


    # Enter a parse tree produced by CParser#statement_list.
    # @param  ctx Type: CParser.Statement_listContext
    def enterStatement_list(self,ctx):
        pass

    # Exit a parse tree produced by CParser#statement_list.
    # @param  ctx Type: CParser.Statement_listContext
    def exitStatement_list(self,ctx):
        pass


    # Enter a parse tree produced by CParser#expression_statement.
    # @param  ctx Type: CParser.Expression_statementContext
    def enterExpression_statement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#expression_statement.
    # @param  ctx Type: CParser.Expression_statementContext
    def exitExpression_statement(self,ctx):
        pass


    # Enter a parse tree produced by CParser#selection_statement.
    # @param  ctx Type: CParser.Selection_statementContext
    def enterSelection_statement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#selection_statement.
    # @param  ctx Type: CParser.Selection_statementContext
    def exitSelection_statement(self,ctx):
        pass


    # Enter a parse tree produced by CParser#iteration_statement.
    # @param  ctx Type: CParser.Iteration_statementContext
    def enterIteration_statement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#iteration_statement.
    # @param  ctx Type: CParser.Iteration_statementContext
    def exitIteration_statement(self,ctx):
        pass


    # Enter a parse tree produced by CParser#jump_statement.
    # @param  ctx Type: CParser.Jump_statementContext
    def enterJump_statement(self,ctx):
        pass

    # Exit a parse tree produced by CParser#jump_statement.
    # @param  ctx Type: CParser.Jump_statementContext
    def exitJump_statement(self,ctx):
        pass


