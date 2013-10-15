I-Logix-RPY-Archive version 8.0.1 Modeler C++ 757343
{ IProject 
	- _id = GUID be26d523-ae44-4436-934b-34389a448a2f;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 7;
			- value = 
			{ IPropertySubject 
				- _Name = "CG";
				- Metaclasses = { IRPYRawContainer 
					- size = 7;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "CGGeneral";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "IgnoreGuardedOperationVisibility";
								- _Value = "True";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Component";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "InitializationScheme";
								- _Value = "ByPackage";
								- _Type = Enum;
								- _ExtraTypeInfo = "ByPackage, ByComponent";
							}
							{ IProperty 
								- _Name = "RelatedComponentsIncludePathInMakefile";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Configuration";
						- Properties = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IProperty 
								- _Name = "AddExplicitInitialInstancesToScope";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "RemoveWhiteSpacesInBuildFile";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "StrictExternalElementsGeneration";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "SupportExternalElementsInScope";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "File";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "IncludeScheme";
								- _Value = "RelativeToConfiguration";
								- _Type = Enum;
								- _ExtraTypeInfo = "RelativeToConfiguration, LocalOnly";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Operation";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "EnableInMethodBroker";
								- _Value = "True";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Relation";
						- Properties = { IRPYRawContainer 
							- size = 6;
							- value = 
							{ IProperty 
								- _Name = "ClearGenerate";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "DeleteComponentGenerate";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "FilledDiamondScheme";
								- _Value = "Aggregation";
								- _Type = Enum;
								- _ExtraTypeInfo = "Aggregation, Composition";
							}
							{ IProperty 
								- _Name = "GetEndGenerate";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "InstanceBasedLinking";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "RemoveGenerate";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Type";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Animate";
								- _Value = "Force";
								- _Type = Enum;
								- _ExtraTypeInfo = "Force,True,False";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "CPP_CG";
				- Metaclasses = { IRPYRawContainer 
					- size = 8;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Attribute";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "AccessorGenerate";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "MarkPrologEpilogInAnnotations";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "None, Ignore, Auto";
							}
							{ IProperty 
								- _Name = "MutatorGenerate";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Class";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "Embeddable";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "IsReactiveInterface";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "MarkPrologEpilogInAnnotations";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "None, Ignore, Auto";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Configuration";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "MarkPrologEpilogInAnnotations";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "None, Ignore, Auto";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Dependency";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "MarkPrologEpilogInAnnotations";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "None, Ignore, Auto";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Operation";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "MarkPrologEpilogInAnnotations";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "None, Ignore, Auto";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Package";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "MarkPrologEpilogInAnnotations";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "None, Ignore, Auto";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Relation";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ImplementWithStaticArray";
								- _Value = "Default";
								- _Type = Enum;
								- _ExtraTypeInfo = "Default,FixedAndBounded";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Type";
						- Properties = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IProperty 
								- _Name = "In";
								- _Value = "$type";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "InOut";
								- _Value = "$type";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Out";
								- _Value = "$type";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "ReturnType";
								- _Value = "$type";
								- _Type = String;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "CPP_ReverseEngineering";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "ImplementationTrait";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "AnalyzeIncludeFiles";
								- _Value = "AllIncludes";
								- _Type = Enum;
								- _ExtraTypeInfo = "IgnoreIncludes,OnlyLogicalHeader,OnlyFromSelected,AllIncludes";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "CPP_Roundtrip";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "General";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "RoundtripScheme";
								- _Value = "Basic";
								- _Type = Enum;
								- _ExtraTypeInfo = "Full,Basic";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "General";
				- Metaclasses = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Graphics";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "DragOnContourOnly";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "Tool_tips";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Model";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "AutoSaveInterval";
								- _Value = "0";
								- _Type = Int;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "SequenceDiagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "General";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ClassCentricMode";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "CleanupRealized";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "RealizeMessages";
								- _Value = "True";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "InstanceLine";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "spacing_units";
								- _Value = "3";
								- _Type = Int;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "TestConductor";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "SequenceDiagram";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "ActivationCondition";
								- _Value = "TRUE";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Parameter";
								- _Value = "";
								- _Type = String;
							}
						}
					}
				}
			}
		}
	}
	- _name = "elevator";
	- _objectCreation = "199716304020061399001019";
	- _umlDependencyID = "2416";
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Default.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Default";
		- _id = OLDID 16466857 1;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "gui.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "gui";
		- _id = GUID fbd6b39c-df11-11d2-ab10-0010a4f1d0f6;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 6;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 0;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "3";
			- _count = 0;
		}
		{ IMultiplicityItem 
			- _name = "NUMBER_OF_ELEVATORS";
			- _count = 0;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 6;
		- value = 
		{ ISubsystem 
			- fileName = "Default";
			- _id = OLDID 16466857 1;
		}
		{ ISubsystem 
			- fileName = "ElevatorPkg";
			- _id = OLDID 3257293 1;
		}
		{ IProfile 
			- fileName = "Pre60GESkin";
			- _id = GUID f2014435-7d08-4cee-b400-4c602d0d92de;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre61Cpp";
			- _id = GUID 2a155864-f668-4216-8df4-2b4be001edc5;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre61M1Cpp";
			- _id = GUID d4ee5b94-9567-4f9e-a279-72bbe2a5baa0;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre70Cpp";
			- _id = GUID d9191aaa-ccb0-4509-a965-04c49ac9fcdc;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ IDiagram 
			- fileName = "host_configuration";
			- _id = OLDID 11675727 1;
			- _name = "host configuration";
		}
		{ IDiagram 
			- fileName = "overview";
			- _id = OLDID 407145 1;
		}
	}
	- MSCS = { IRPYRawContainer 
		- size = 6;
		- value = 
		{ IMSC 
			- fileName = "call_when_elevator_idle_above_or_below_floor";
			- _id = OLDID 5164966 1;
			- _name = "call when elevator idle above or below floor";
		}
		{ IMSC 
			- fileName = "call_when_elevator_idle_at_floor";
			- _id = OLDID 5215479 1;
			- _name = "call when elevator idle at floor";
		}
		{ IMSC 
			- fileName = "call_when_elevator_moving_down_above_floor";
			- _id = OLDID 5197543 1;
			- _name = "call when elevator moving down above floor";
		}
		{ IMSC 
			- fileName = "call_when_elevator_moving_down_below_floor";
			- _id = OLDID 5248516 1;
			- _name = "call when elevator moving down below floor";
		}
		{ IMSC 
			- fileName = "call_when_elevator_moving_up_above_floor";
			- _id = OLDID 5180278 1;
			- _name = "call when elevator moving up above floor";
		}
		{ IMSC 
			- fileName = "call_when_elevator_moving_up_below_floor";
			- _id = OLDID 5258921 1;
			- _name = "call when elevator moving up below floor";
		}
	}
	- Components = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IComponent 
			- fileName = "gui";
			- _id = GUID fbd6b39c-df11-11d2-ab10-0010a4f1d0f6;
		}
		{ IComponent 
			- fileName = "guilib";
			- _id = GUID fbd6b3a2-df11-11d2-ab10-0010a4f1d0f6;
		}
		{ IComponent 
			- fileName = "host";
			- _id = GUID fbd6b3ae-df11-11d2-ab10-0010a4f1d0f6;
		}
		{ IComponent 
			- fileName = "target";
			- _id = GUID fbd6b3b4-df11-11d2-ab10-0010a4f1d0f6;
		}
	}
	- UCDiagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IUCDiagram 
			- fileName = "main_uses";
			- _id = OLDID 2190669 1;
			- _name = "main uses";
		}
	}
	- CollaborationDiagrams = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ ICollaborationDiagram 
			- fileName = "call_when_elevator_idle_above_or_below_floor";
			- _id = GUID 9c0762d4-4a4e-4e01-b0fc-2ce73a67cbf1;
			- _name = "call when elevator idle above or below floor";
		}
		{ ICollaborationDiagram 
			- fileName = "call_when_elevator_idle_at_floor";
			- _id = GUID 6d583337-9cfb-44e9-a994-6ff99888b538;
			- _name = "call when elevator idle at floor";
		}
	}
}

