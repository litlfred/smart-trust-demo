export type ScreenId = 'S1' | 'S2' | 'S3' | 'S4' | 'S5' | 'S6' | 'S7' | 'S8';

export type DeviceType = 'DESKTOP' | 'TABLET' | 'MOBILE';

export type ActiveTab = 'journeys' | 'screens';

export interface JourneyStage {
  id: string;
  screenId: ScreenId;
  stageCode: string; // J1, J2a, J2b, J3a, J3b, J4.0a, J4.0b, J4.1
  title: string;
  subtitle: string;
  country: 'Thailand' | 'Lao PDR' | 'Cross-Border';
  countryCode: 'THA' | 'LAO';
  location: string;
  actor: string;
  actorRole: string;
  appConfig: string;
  deviceType: DeviceType;
  timeline: string;
  statusBadge: {
    label: string;
    variant: 'verified' | 'unverified' | 'warning' | 'info' | 'tampered';
  };
  summary: string;
  learningObjective: string;
}

export interface PatientDemographics {
  infantName: string;
  motherName: string;
  fatherName: string;
  householdId: string;
  infantDob: string;
  birthHospital: string;
  nationality: string;
  motherAge: number;
  fatherAge: number;
}

export interface ImmunizationRecord {
  id: string;
  vaccineName: string;
  targetDisease: string;
  dateAdministered: string;
  countryAdministered: string;
  facility: string;
  lotNumber: string;
  preQualCode: string;
  laoEpiCode?: string;
  primarySource: boolean;
  status: 'completed' | 'unverified' | 'verified';
  doseNumber: number;
  signedBy?: string;
  keyId?: string;
  provenanceAttached: boolean;
}

export interface GDHCNTrustDetails {
  keyId: string;
  issuerCountry: string;
  issuerName: string;
  status: 'valid' | 'tampered' | 'expired';
  algorithm: string;
  dscValidity: string;
  cborHeader: {
    alg: string;
    kid: string;
    iss: string;
  };
}
