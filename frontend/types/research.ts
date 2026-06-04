export interface Source {
  title: string;
  url: string;
}

export interface ResearchResponse {
  answer: string;
  confidence: number;
  sources: Source[];
}