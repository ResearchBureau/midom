"""Useful subsets of all non-private dicom sets"""


class ImageTypeIDSubspace:

        """Tags used to determine what type of DICOM image this is.
        Used to match burnt-in information locations
        """

        tags = ["BurnedInAnnotation",
            "CodeMeaning",
            "Columns",
            "CommentsOnRadiationDose",
            "ConvolutionKernel",
            "ImageComments",
            "ImageType",
            "InstanceNumber",
            "Modality",
            "Manufacturer",
            "ManufacturerModelName",
            "ProtocolName",
            "Rows",
            "SeriesDescription",
            "StationName",
            "SoftwareVersions"]


class E1_1Subspace:
        """All non-private DICOM tags mentioned in DICOM PS3.15 table E.1-1 -
        Application Level Confidentiality Profile Attributes. If a tag is in this
        list, it means the official DICOM deidentification rules have something to
        say about how to handle that tag.

        Notes
        -----
        Does not include "Private Elements". This is in table E.1-1 but is not a real
        dicom tag keyword. Private elements should be processed separately.
        """
        tags = ["AccessionNumber",
                "AcquisitionComments",
                "AcquisitionContextSequence",
                "AcquisitionDate",
                "AcquisitionDateTime",
                "AcquisitionDeviceProcessingDescription",
                "AcquisitionFieldOfViewLabel",
                "AcquisitionProtocolDescription",
                "AcquisitionTime",
                "AcquisitionUID",
                "ActualHumanPerformersSequence",
                "AdditionalPatientHistory",
                "AddressTrial",
                "AdmissionID",
                "AdmittingDate",
                "AdmittingDiagnosesCodeSequence",
                "AdmittingDiagnosesDescription",
                "AdmittingTime",
                "AffectedSOPInstanceUID",
                "Allergies",
                "AnnotationGroupDescription",
                "AnnotationGroupLabel",
                "AnnotationGroupUID",
                "ApprovalStatusDateTime",
                "Arbitrary",
                "AssertionDateTime",
                "AssertionExpirationDateTime",
                "AttributeModificationDateTime",
                "AuthorObserverSequence",
                "BarcodeValue",
                "BeamDescription",
                "BeamHoldTransitionDateTime",
                "BolusDescription",
                "BranchOfService",
                "CalibrationDate",
                "CalibrationDateTime",
                "CalibrationTime",
                "CameraOwnerName",
                "CassetteID",
                "CertificateOfSigner",
                "CertifiedTimestamp",
                "ClinicalTrialCoordinatingCenterName",
                "ClinicalTrialProtocolEthicsCommitteeApprovalNumber",
                "ClinicalTrialProtocolEthicsCommitteeName",
                "ClinicalTrialProtocolID",
                "ClinicalTrialProtocolName",
                "ClinicalTrialSeriesDescription",
                "ClinicalTrialSeriesID",
                "ClinicalTrialSiteID",
                "ClinicalTrialSiteName",
                "ClinicalTrialSponsorName",
                "ClinicalTrialSubjectID",
                "ClinicalTrialSubjectReadingID",
                "ClinicalTrialTimePointDescription",
                "ClinicalTrialTimePointID",
                "CommentsOnRadiationDose",
                "CommentsOnThePerformedProcedureStep",
                "CompensatorDescription",
                "ConcatenationUID",
                "ConceptualVolumeCombinationDescription",
                "ConceptualVolumeDescription",
                "ConceptualVolumeUID",
                "ConfidentialityConstraintOnPatientDataDescription",
                "ConstituentConceptualVolumeUID",
                "ConsultingPhysicianIdentificationSequence",
                "ConsultingPhysicianName",
                "ContainerComponentID",
                "ContainerDescription",
                "ContainerIdentifier",
                "ContentCreatorIdentificationCodeSequence",
                "ContentCreatorName",
                "ContentDate",
                "ContentSequence",
                "ContentTime",
                "ContextGroupLocalVersion",
                "ContextGroupVersion",
                "ContrastBolusAgent",
                "ContrastBolusStartTime",
                "ContrastBolusStopTime",
                "ContributionDateTime",
                "ContributionDescription",
                "CountryOfResidence",
                "CreationDate",
                "CreationTime",
                "CurrentObserverTrial",
                "CurrentPatientLocation",
                "CurveDate",
                "CurveTime",
                "CustodialOrganizationSequence",
                "DataSetTrailingPadding",
                "Date",
                "DateOfDocumentOrVerbalTransactionTrial",
                "DateOfLastCalibration",
                "DateOfLastDetectorCalibration",
                "DateOfSecondaryCapture",
                "DateTime",
                "DateTimeOfLastCalibration",
                "DecayCorrectionDateTime",
                "DecompositionDescription",
                "DerivationDescription",
                "DestinationAE",
                "DetectorID",
                "DeviceAlternateIdentifier",
                "DeviceDescription",
                "DeviceLabel",
                "DeviceSerialNumber",
                "DeviceSettingDescription",
                "DeviceUID",
                "DigitalSignatureDateTime",
                "DigitalSignaturesSequence",
                "DigitalSignatureUID",
                "DimensionOrganizationUID",
                "DischargeDate",
                "DischargeDiagnosisDescription",
                "DischargeTime",
                "DisplacementReferenceLabel",
                "DistributionAddress",
                "DistributionName",
                "DoseReferenceDescription",
                "DoseReferenceUID",
                "DosimetricObjectiveUID",
                "EffectiveDateTime",
                "EncapsulatedDocument",
                "EndAcquisitionDateTime",
                "EntityDescription",
                "EntityLabel",
                "EntityLongLabel",
                "EntityName",
                "EquipmentFrameOfReferenceDescription",
                "EthicsCommitteeApprovalEffectivenessEndDate",
                "EthicsCommitteeApprovalEffectivenessStartDate",
                "EthnicGroup",
                "ExclusionStartDateTime",
                "ExpectedCompletionDateTime",
                "FailedSOPInstanceUIDList",
                "FiducialUID",
                "FillerOrderNumberImagingServiceRequest",
                "FilterLookupTableDescription",
                "FindingsGroupRecordingDateTrial",
                "FindingsGroupRecordingTimeTrial",
                "FirstTreatmentDate",
                "FixationDeviceDescription",
                "FlowIdentifier",
                "FlowIdentifierSequence",
                "FractionationNotes",
                "FractionGroupDescription",
                "FrameAcquisitionDateTime",
                "FrameComments",
                "FrameOfReferenceUID",
                "FrameOriginTimestamp",
                "FrameReferenceDateTime",
                "FunctionalSyncPulse",
                "GantryID",
                "GeneratorID",
                "GPSAltitude",
                "GPSAltitudeRef",
                "GPSAreaInformation",
                "GPSDateStamp",
                "GPSDestBearing",
                "GPSDestBearingRef",
                "GPSDestDistance",
                "GPSDestDistanceRef",
                "GPSDestLatitude",
                "GPSDestLatitudeRef",
                "GPSDestLongitude",
                "GPSDestLongitudeRef",
                "GPSDifferential",
                "GPSDOP",
                "GPSImgDirection",
                "GPSImgDirectionRef",
                "GPSLatitude",
                "GPSLatitudeRef",
                "GPSLongitude",
                "GPSLongitudeRef",
                "GPSMapDatum",
                "GPSMeasureMode",
                "GPSProcessingMethod",
                "GPSSatellites",
                "GPSSpeed",
                "GPSSpeedRef",
                "GPSStatus",
                "GPSTimeStamp",
                "GPSTrack",
                "GPSTrackRef",
                "GPSVersionID",
                "GraphicAnnotationSequence",
                "HangingProtocolCreationDateTime",
                "HL7DocumentEffectiveTime",
                "HumanPerformerName",
                "HumanPerformerOrganization",
                "IconImageSequence",
                "IdentifyingComments",
                "ImageComments",
                "ImagePresentationComments",
                "ImagingServiceRequestComments",
                "ImpedanceMeasurementDateTime",
                "Impressions",
                "InformationIssueDateTime",
                "InstanceCoercionDateTime",
                "InstanceCreationDate",
                "InstanceCreationTime",
                "InstanceCreatorUID",
                "InstanceOriginStatus",
                "InstitutionAddress",
                "InstitutionalDepartmentName",
                "InstitutionalDepartmentTypeCodeSequence",
                "InstitutionCodeSequence",
                "InstitutionName",
                "InstructionPerformedDateTime",
                "InsurancePlanIdentification",
                "IntendedFractionStartTime",
                "IntendedPhaseEndDate",
                "IntendedPhaseStartDate",
                "IntendedRecipientsOfResultsIdentificationSequence",
                "InterlockDateTime",
                "InterlockDescription",
                "InterlockOriginDescription",
                "InterpretationApprovalDate",
                "InterpretationApprovalTime",
                "InterpretationApproverSequence",
                "InterpretationAuthor",
                "InterpretationDiagnosisDescription",
                "InterpretationID",
                "InterpretationIDIssuer",
                "InterpretationRecordedDate",
                "InterpretationRecordedTime",
                "InterpretationRecorder",
                "InterpretationText",
                "InterpretationTranscriber",
                "InterpretationTranscriptionDate",
                "InterpretationTranscriptionTime",
                "InterventionDrugStartTime",
                "InterventionDrugStopTime",
                "IrradiationEventUID",
                "IssueDateOfImagingServiceRequest",
                "IssuerOfAdmissionID",
                "IssuerOfAdmissionIDSequence",
                "IssuerOfPatientID",
                "IssuerOfServiceEpisodeID",
                "IssuerOfServiceEpisodeIDSequence",
                "IssuerOfTheContainerIdentifierSequence",
                "IssuerOfTheSpecimenIdentifierSequence",
                "IssueTimeOfImagingServiceRequest",
                "LabelText",
                "LargePaletteColorLookupTableUID",
                "LastMenstrualDate",
                "LensMake",
                "LensModel",
                "LensSerialNumber",
                "LensSpecification",
                "LongDeviceDescription",
                "MAC",
                "MakerNote",
                "ManufacturerDeviceClassUID",
                "ManufacturerDeviceIdentifier",
                "MediaStorageSOPInstanceUID",
                "MedicalAlerts",
                "MedicalRecordLocator",
                "MilitaryRank",
                "ModifiedAttributesSequence",
                "ModifiedImageDate",
                "ModifiedImageDescription",
                "ModifiedImageTime",
                "ModifyingDeviceID",
                "ModifyingSystem",
                "MostRecentTreatmentDate",
                "MultienergyAcquisitionDescription",
                "MultiplexGroupUID",
                "NameOfPhysiciansReadingStudy",
                "NamesOfIntendedRecipientsOfResults",
                "NetworkID",
                "NonconformingDataElementValue",
                "NonconformingModifiedAttributesSequence",
                "ObservationDateTime",
                "ObservationDateTrial",
                "ObservationStartDateTime",
                "ObservationSubjectUIDTrial",
                "ObservationTimeTrial",
                "ObservationUID",
                "Occupation",
                "OperatorIdentificationSequence",
                "OperatorsName",
                "OrderCallbackPhoneNumber",
                "OrderCallbackTelecomInformation",
                "OrderEnteredBy",
                "OrderEntererLocation",
                "OriginalAttributesSequence",
                "Originator",
                "OtherPatientIDs",
                "OtherPatientIDsSequence",
                "OtherPatientNames",
                "OverlayComments",
                "OverlayData",
                "OverlayDate",
                "OverlayTime",
                "OverrideDateTime",
                "PaletteColorLookupTableUID",
                "ParticipantSequence",
                "ParticipationDateTime",
                "PatientAddress",
                "PatientAge",
                "PatientBirthDate",
                "PatientBirthName",
                "PatientBirthTime",
                "PatientComments",
                "PatientID",
                "PatientInstitutionResidence",
                "PatientInsurancePlanCodeSequence",
                "PatientMotherBirthName",
                "PatientName",
                "PatientPrimaryLanguageCodeSequence",
                "PatientPrimaryLanguageModifierCodeSequence",
                "PatientReligiousPreference",
                "PatientSetupPhotoDescription",
                "PatientSetupUID",
                "PatientSex",
                "PatientSexNeutered",
                "PatientSize",
                "PatientState",
                "PatientTelecomInformation",
                "PatientTelephoneNumbers",
                "PatientTransportArrangements",
                "PatientTreatmentPreparationMethodDescription",
                "PatientTreatmentPreparationProcedureParameterDescription",
                "PatientWeight",
                "PerformedLocation",
                "PerformedProcedureStepDescription",
                "PerformedProcedureStepEndDate",
                "PerformedProcedureStepEndDateTime",
                "PerformedProcedureStepEndTime",
                "PerformedProcedureStepID",
                "PerformedProcedureStepStartDate",
                "PerformedProcedureStepStartDateTime",
                "PerformedProcedureStepStartTime",
                "PerformedStationAETitle",
                "PerformedStationGeographicLocationCodeSequence",
                "PerformedStationName",
                "PerformedStationNameCodeSequence",
                "PerformingPhysicianIdentificationSequence",
                "PerformingPhysicianName",
                "PersonAddress",
                "PersonIdentificationCodeSequence",
                "PersonName",
                "PersonTelecomInformation",
                "PersonTelephoneNumbers",
                "PhysicianApprovingInterpretation",
                "PhysiciansOfRecord",
                "PhysiciansOfRecordIdentificationSequence",
                "PhysiciansReadingStudyIdentificationSequence",
                "PlacerOrderNumberImagingServiceRequest",
                "PlateID",
                "PositionAcquisitionTemplateDescription",
                "PositionAcquisitionTemplateName",
                "PregnancyStatus",
                "PreMedication",
                "PrescriptionDescription",
                "PrescriptionNotes",
                "PrescriptionNotesSequence",
                "PresentationCreationDate",
                "PresentationCreationTime",
                "PresentationDisplayCollectionUID",
                "PresentationSequenceCollectionUID",
                "PriorTreatmentDoseDescription",
                "ProcedureStepCancellationDateTime",
                "ProductExpirationDateTime",
                "ProtocolName",
                "PyramidDescription",
                "PyramidLabel",
                "PyramidUID",
                "RadiationDoseIdentificationLabel",
                "RadiationDoseInVivoMeasurementLabel",
                "RadiationGenerationModeDescription",
                "RadiationGenerationModeLabel",
                "RadiopharmaceuticalStartDateTime",
                "RadiopharmaceuticalStartTime",
                "RadiopharmaceuticalStopDateTime",
                "RadiopharmaceuticalStopTime",
                "ReasonForOmissionDescription",
                "ReasonForRequestedProcedureCodeSequence",
                "ReasonForStudy",
                "ReasonForSuperseding",
                "ReasonForTheAttributeModification",
                "ReasonForTheImagingServiceRequest",
                "ReasonForTheRequestedProcedure",
                "ReasonForVisit",
                "ReasonForVisitCodeSequence",
                "ReceivingAE",
                "RecordedRTControlPointDateTime",
                "ReferencedConceptualVolumeUID",
                "ReferencedDateTime",
                "ReferencedDigitalSignatureSequence",
                "ReferencedDoseReferenceUID",
                "ReferencedDosimetricObjectiveUID",
                "ReferencedFiducialsUID",
                "ReferencedFrameOfReferenceUID",
                "ReferencedGeneralPurposeScheduledProcedureStepTransactionUID",
                "ReferencedImageSequence",
                "ReferencedObservationUIDTrial",
                "ReferencedPatientAliasSequence",
                "ReferencedPatientPhotoSequence",
                "ReferencedPatientSequence",
                "ReferencedPerformedProcedureStepSequence",
                "ReferencedSOPInstanceMACSequence",
                "ReferencedSOPInstanceUID",
                "ReferencedSOPInstanceUIDInFile",
                "ReferencedStudySequence",
                "ReferencedTreatmentPositionGroupUID",
                "ReferringPhysicianAddress",
                "ReferringPhysicianIdentificationSequence",
                "ReferringPhysicianName",
                "ReferringPhysicianTelephoneNumbers",
                "RegionOfResidence",
                "RelatedFrameOfReferenceUID",
                "RequestAttributesSequence",
                "RequestedContrastAgent",
                "RequestedProcedureComments",
                "RequestedProcedureDescription",
                "RequestedProcedureID",
                "RequestedProcedureLocation",
                "RequestedSeriesDescription",
                "RequestedSOPInstanceUID",
                "RequestingAE",
                "RequestingPhysician",
                "RequestingService",
                "RespiratoryMotionCompensationTechniqueDescription",
                "ResponsibleOrganization",
                "ResponsiblePerson",
                "ResultsComments",
                "ResultsDistributionListSequence",
                "ResultsID",
                "ResultsIDIssuer",
                "RetrieveAETitle",
                "ReviewDate",
                "ReviewerName",
                "ReviewTime",
                "ROICreatorSequence",
                "ROIDateTime",
                "ROIDescription",
                "ROIGenerationDescription",
                "ROIInterpreter",
                "ROIInterpreterSequence",
                "ROIName",
                "ROIObservationDateTime",
                "ROIObservationDescription",
                "ROIObservationLabel",
                "RTAccessoryDeviceSlotID",
                "RTAccessoryHolderSlotID",
                "RTPhysicianIntentNarrative",
                "RTPlanDate",
                "RTPlanDescription",
                "RTPlanLabel",
                "RTPlanName",
                "RTPlanTime",
                "RTPrescriptionLabel",
                "RTToleranceSetLabel",
                "RTTreatmentApproachLabel",
                "RTTreatmentPhaseUID",
                "SafePositionExitDate",
                "SafePositionExitTime",
                "SafePositionReturnDate",
                "SafePositionReturnTime",
                "ScheduledAdmissionDate",
                "ScheduledAdmissionTime",
                "ScheduledDischargeDate",
                "ScheduledDischargeTime",
                "ScheduledHumanPerformersSequence",
                "ScheduledPatientInstitutionResidence",
                "ScheduledPerformingPhysicianIdentificationSequence",
                "ScheduledPerformingPhysicianName",
                "ScheduledProcedureStepDescription",
                "ScheduledProcedureStepEndDate",
                "ScheduledProcedureStepEndTime",
                "ScheduledProcedureStepExpirationDateTime",
                "ScheduledProcedureStepID",
                "ScheduledProcedureStepLocation",
                "ScheduledProcedureStepModificationDateTime",
                "ScheduledProcedureStepStartDate",
                "ScheduledProcedureStepStartDateTime",
                "ScheduledProcedureStepStartTime",
                "ScheduledStationAETitle",
                "ScheduledStationGeographicLocationCodeSequence",
                "ScheduledStationName",
                "ScheduledStationNameCodeSequence",
                "ScheduledStudyLocation",
                "ScheduledStudyLocationAETitle",
                "ScheduledStudyStartDate",
                "ScheduledStudyStartTime",
                "ScheduledStudyStopDate",
                "ScheduledStudyStopTime",
                "SelectorAEValue",
                "SelectorASValue",
                "SelectorDAValue",
                "SelectorDTValue",
                "SelectorLOValue",
                "SelectorLTValue",
                "SelectorOBValue",
                "SelectorPNValue",
                "SelectorSHValue",
                "SelectorSTValue",
                "SelectorTMValue",
                "SelectorUNValue",
                "SelectorURValue",
                "SelectorUTValue",
                "SeriesDate",
                "SeriesDescription",
                "SeriesInstanceUID",
                "SeriesTime",
                "ServiceEpisodeDescription",
                "ServiceEpisodeID",
                "SetupTechniqueDescription",
                "ShieldingDeviceDescription",
                "SlideIdentifier",
                "SmokingStatus",
                "SOPAuthorizationDateTime",
                "SOPInstanceUID",
                "SourceConceptualVolumeUID",
                "SourceEndDateTime",
                "SourceFrameOfReferenceUID",
                "SourceIdentifier",
                "SourceImageSequence",
                "SourceManufacturer",
                "SourceOfPreviousValues",
                "SourceSerialNumber",
                "SourceStartDateTime",
                "SourceStrengthReferenceDate",
                "SourceStrengthReferenceTime",
                "SpecialNeeds",
                "SpecimenAccessionNumber",
                "SpecimenDetailedDescription",
                "SpecimenIdentifier",
                "SpecimenPreparationSequence",
                "SpecimenShortDescription",
                "SpecimenUID",
                "StartAcquisitionDateTime",
                "StationAETitle",
                "StationName",
                "StorageMediaFileSetUID",
                "StructureSetDate",
                "StructureSetDescription",
                "StructureSetLabel",
                "StructureSetName",
                "StructureSetTime",
                "StudyArrivalDate",
                "StudyArrivalTime",
                "StudyComments",
                "StudyCompletionDate",
                "StudyCompletionTime",
                "StudyDate",
                "StudyDescription",
                "StudyID",
                "StudyIDIssuer",
                "StudyInstanceUID",
                "StudyReadDate",
                "StudyReadTime",
                "StudyTime",
                "StudyVerifiedDate",
                "StudyVerifiedTime",
                "SubstanceAdministrationDateTime",
                "SynchronizationFrameOfReferenceUID",
                "TableTopPositionAlignmentUID",
                "TargetUID",
                "TelephoneNumberTrial",
                "TemplateExtensionCreatorUID",
                "TemplateExtensionOrganizationUID",
                "TemplateLocalVersion",
                "TemplateVersion",
                "TextComments",
                "TextString",
                "Time",
                "TimeOfDocumentCreationOrVerbalTransactionTrial",
                "TimeOfLastCalibration",
                "TimeOfLastDetectorCalibration",
                "TimeOfSecondaryCapture",
                "TimezoneOffsetFromUTC",
                "TopicAuthor",
                "TopicKeywords",
                "TopicSubject",
                "TopicTitle",
                "TrackingUID",
                "TransactionUID",
                "TransducerIdentificationSequence",
                "TreatmentControlPointDate",
                "TreatmentControlPointTime",
                "TreatmentDate",
                "TreatmentMachineName",
                "TreatmentPositionGroupLabel",
                "TreatmentPositionGroupUID",
                "TreatmentSessionUID",
                "TreatmentSite",
                "TreatmentSites",
                "TreatmentTechniqueNotes",
                "TreatmentTime",
                "TreatmentToleranceViolationDateTime",
                "TreatmentToleranceViolationDescription",
                "UDISequence",
                "UID",
                "UniqueDeviceIdentifier",
                "UserContentLabel",
                "UserContentLongLabel",
                "VerbalSourceIdentifierCodeSequenceTrial",
                "VerbalSourceTrial",
                "VerificationDateTime",
                "VerifyingObserverIdentificationCodeSequence",
                "VerifyingObserverName",
                "VerifyingObserverSequence",
                "VerifyingOrganization",
                "VisitComments",
                "WaveformFilterDescription",
                "XRayDetectorID",
                "XRayDetectorLabel",
                "XRaySourceID"]